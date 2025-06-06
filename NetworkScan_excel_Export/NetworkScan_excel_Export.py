#!/usr/bin/env python3
"""
Scanner de réseau multiplateforme (Linux, Mac, Windows)
Scanne le réseau local et exporte les informations dans un fichier Excel
"""

import subprocess
import platform
import socket
import re
import ipaddress
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
from datetime import datetime
import netifaces
import psutil

class NetworkScanner:
    def __init__(self):
        self.os_type = platform.system().lower()
        self.devices = []
        self.lock = threading.Lock()
        
    def get_local_networks(self):
        """Récupère les réseaux locaux disponibles"""
        networks = []
        try:
            # Méthode 1: Utiliser netifaces
            for interface in netifaces.interfaces():
                try:
                    addrs = netifaces.ifaddresses(interface)
                    if netifaces.AF_INET in addrs:
                        for addr_info in addrs[netifaces.AF_INET]:
                            ip = addr_info.get('addr')
                            netmask = addr_info.get('netmask')
                            if ip and netmask and not ip.startswith('127.'):
                                network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                                if not network.is_loopback:
                                    networks.append(str(network.network_address) + '/' + str(network.prefixlen))
                except:
                    continue
        except:
            pass
            
        # Méthode 2: Fallback avec psutil
        if not networks:
            try:
                for interface, addrs in psutil.net_if_addrs().items():
                    for addr in addrs:
                        if addr.family == socket.AF_INET and not addr.address.startswith('127.'):
                            try:
                                network = ipaddress.IPv4Network(f"{addr.address}/{addr.netmask}", strict=False)
                                networks.append(str(network.network_address) + '/' + str(network.prefixlen))
                            except:
                                continue
            except:
                pass
                
        # Méthode 3: Réseaux communs par défaut
        if not networks:
            networks = ['192.168.1.0/24', '192.168.0.0/24', '10.0.0.0/24']
            
        return list(set(networks))
    
    def is_host_alive(self, ip):
        """Vérifie si un hôte est accessible via ping"""
        try:
            if self.os_type == "windows":
                cmd = ["ping", "-n", "1", "-w", "1000", str(ip)]
            else:
                cmd = ["ping", "-c", "1", "-W", "1", str(ip)]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
            return result.returncode == 0
        except:
            return False
    
    def get_mac_address(self, ip):
        """Récupère l'adresse MAC d'une IP"""
        try:
            if self.os_type == "windows":
                cmd = ["arp", "-a", str(ip)]
            else:
                cmd = ["arp", "-n", str(ip)]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=2)
            
            if result.returncode == 0:
                # Recherche d'adresse MAC dans la sortie
                mac_pattern = r'([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}'
                match = re.search(mac_pattern, result.stdout)
                if match:
                    return match.group(0).upper().replace('-', ':')
        except:
            pass
        return "N/A"
    
    def get_hostname(self, ip):
        """Récupère le nom d'hôte d'une IP"""
        try:
            hostname = socket.gethostbyaddr(str(ip))[0]
            return hostname
        except:
            return "N/A"
    
    def get_open_ports(self, ip, common_ports=None):
        """Scanne les ports ouverts (ports communs seulement pour la rapidité)"""
        if common_ports is None:
            common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1723, 3389, 5900]
        
        open_ports = []
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((str(ip), port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                continue
        
        return open_ports
    
    def get_device_vendor(self, mac):
        """Tente d'identifier le fabricant basé sur l'adresse MAC"""
        if mac == "N/A":
            return "N/A"
        
        # Dictionnaire simplifié des OUI (Organizationally Unique Identifier)
        oui_dict = {
            "00:50:56": "VMware",
            "08:00:27": "VirtualBox",
            "00:0C:29": "VMware",
            "00:1C:42": "Parallels",
            "DC:A6:32": "Raspberry Pi",
            "B8:27:EB": "Raspberry Pi",
            "E4:5F:01": "Raspberry Pi",
            "00:16:3E": "Xen",
            "00:03:FF": "Microsoft",
            "00:D0:C9": "Intel",
            "00:E0:4C": "Realtek",
            "00:90:27": "Intel",
            "AC:DE:48": "Intel",
            "F0:79:59": "Intel"
        }
        
        mac_prefix = mac[:8].upper()
        return oui_dict.get(mac_prefix, "Inconnu")
    
    def scan_host(self, ip):
        """Scanne un hôte spécifique"""
        try:
            if self.is_host_alive(ip):
                print(f"Scanning {ip}...")
                
                mac = self.get_mac_address(ip)
                hostname = self.get_hostname(ip)
                open_ports = self.get_open_ports(ip)
                vendor = self.get_device_vendor(mac)
                
                device_info = {
                    'IP': str(ip),
                    'MAC': mac,
                    'Hostname': hostname,
                    'Vendor': vendor,
                    'Open_Ports': ', '.join(map(str, open_ports)) if open_ports else "Aucun",
                    'Ports_Count': len(open_ports),
                    'Status': 'Active',
                    'Scan_Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
                with self.lock:
                    self.devices.append(device_info)
                    
        except Exception as e:
            print(f"Erreur lors du scan de {ip}: {e}")
    
    def scan_network(self, network_range):
        """Scanne un réseau complet"""
        try:
            network = ipaddress.IPv4Network(network_range)
            print(f"Scanning network: {network_range}")
            
            # Utiliser ThreadPoolExecutor pour paralléliser le scan
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = [executor.submit(self.scan_host, ip) for ip in network.hosts()]
                
                # Attendre que tous les threads se terminent
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Erreur dans le thread: {e}")
                        
        except Exception as e:
            print(f"Erreur lors du scan du réseau {network_range}: {e}")
    
    def export_to_excel(self, filename="network_scan_results.xlsx"):
        """Exporte les résultats vers un fichier Excel"""
        try:
            if not self.devices:
                print("Aucun appareil trouvé à exporter.")
                return False
            
            df = pd.DataFrame(self.devices)
            
            # Trier par IP
            df['IP_sort'] = df['IP'].apply(lambda x: ipaddress.IPv4Address(x))
            df = df.sort_values('IP_sort').drop('IP_sort', axis=1)
            
            # Créer le fichier Excel avec mise en forme
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Network Scan', index=False)
                
                # Obtenir la feuille de calcul pour la mise en forme
                worksheet = writer.sheets['Network Scan']
                
                # Ajuster la largeur des colonnes
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = min(max_length + 2, 50)
                    worksheet.column_dimensions[column_letter].width = adjusted_width
            
            print(f"Résultats exportés vers: {filename}")
            return True
            
        except Exception as e:
            print(f"Erreur lors de l'export: {e}")
            return False
    
    def run_scan(self):
        """Lance le scan complet"""
        print("Démarrage du scan réseau...")
        print(f"Système d'exploitation détecté: {self.os_type}")
        
        # Récupérer les réseaux locaux
        networks = self.get_local_networks()
        print(f"Réseaux détectés: {networks}")
        
        start_time = time.time()
        
        # Scanner chaque réseau
        for network in networks:
            self.scan_network(network)
        
        end_time = time.time()
        scan_duration = round(end_time - start_time, 2)
        
        print(f"\nScan terminé en {scan_duration} secondes")
        print(f"Nombre d'appareils trouvés: {len(self.devices)}")
        
        # Afficher un résumé
        if self.devices:
            print("\nRésumé des appareils trouvés:")
            for device in self.devices:
                print(f"  {device['IP']} - {device['Hostname']} ({device['MAC']})")
        
        # Exporter vers Excel
        return self.export_to_excel()

def main():
    """Fonction principale"""
    print("=== Scanner de Réseau Multiplateforme ===")
    print("Ce script va scanner votre réseau local et créer un fichier Excel avec les résultats.")
    
    try:
        scanner = NetworkScanner()
        success = scanner.run_scan()
        
        if success:
            print("\n✅ Scan terminé avec succès!")
            print("Le fichier 'network_scan_results.xlsx' a été créé dans le répertoire courant.")
        else:
            print("\n❌ Erreur lors du scan ou de l'export.")
            
    except KeyboardInterrupt:
        print("\n⚠️ Scan interrompu par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")

if __name__ == "__main__":
    main()
