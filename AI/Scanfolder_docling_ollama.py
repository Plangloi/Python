# AI/Scanfolder_docling_ollama.py
# Script to convert PDFs in project folders to Markdown using Docling
# and generate project summaries using Ollama AI.


import os
import subprocess
from pathlib import Path
from docling.document_converter import DocumentConverter

# This script processes all project folders in a specified base path.
# For each project folder, it converts all PDF files to Markdown format
def convert_pdfs_to_markdown(project_path):
    """
    Convert all PDF files in a project folder to Markdown using Docling
    
    Args:
        project_path: Path to the project folder
    
    Returns:
        List of generated markdown file paths
    """
    converter = DocumentConverter()
    markdown_files = []
    
    # Find all PDF files in the project folder
    pdf_files = list(Path(project_path).rglob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {project_path}")
        return markdown_files
    
    print(f"Found {len(pdf_files)} PDF file(s) in {project_path}")
    
    for pdf_file in pdf_files:
        try:
            print(f"Converting {pdf_file.name}...")
            
            # Convert PDF to markdown if md not already exists
            md_file = pdf_file.with_suffix('.md')
            if not md_file.exists():
                result = converter.convert(str(pdf_file))
                markdown_content = result.document.export_to_markdown()
                
                # Write markdown content
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                
                print(f"✓ Created {md_file.name}")
            else:
                print(f"✓ Markdown file already exists for {pdf_file.name}, skipping conversion.")
            
            # Write markdown content
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            markdown_files.append(md_file)
            print(f"✓ Created {md_file.name}")
            
        except Exception as e:
            print(f"✗ Error converting {pdf_file.name}: {e}")
    
    return markdown_files

def generate_project_summary(project_path, markdown_files):
    """
    Generate a project summary using Ollama AI based on markdown files
    
    Args:
        project_path: Path to the project folder
        markdown_files: List of markdown file paths
    """
    if not markdown_files:
        print(f"No markdown files to summarize for {project_path}")
        return
    
    # Combine all markdown content
    combined_content = ""
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            combined_content += f"\n\n=== {md_file.name} ===\n\n"
            combined_content += f.read()
    
    # Prepare prompt for Ollama
    prompt = f"""Based on the following documents from a project, create a comprehensive summary of the project. 
Include:
- Project overview
- Main objectives
- Key findings or conclusions
- Important technical details

Documents:
{combined_content[:15000]}  # Limit content to avoid token limits

Please provide a clear and concise summary:"""
    
    print(f"\nGenerating AI summary for {Path(project_path).name}...")
    
    try:
        # Call Ollama using subprocess
        result = subprocess.run(
            ['ollama', 'run', 'gemma3:4b', prompt],  # Change 'llama2' to your preferred model
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            summary = result.stdout
            
            # Save summary to project folder
            summary_file = Path(project_path) / "PROJECT_SUMMARY.md"
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(f"# Project Summary: {Path(project_path).name}\n\n")
                f.write(f"*Generated from {len(markdown_files)} document(s)*\n\n")
                f.write(summary)
            
            print(f"✓ Summary saved to {summary_file}")
        else:
            print(f"✗ Error from Ollama: {result.stderr}")
            
    except FileNotFoundError:
        print("✗ Ollama not found. Please install Ollama first: https://ollama.ai")
    except subprocess.TimeoutExpired:
        print("✗ Ollama request timed out")
    except Exception as e:
        print(f"✗ Error generating summary: {e}")

def process_projects(base_path):
    """
    Process all project folders in the base path
    
    Args:
        base_path: Path containing project folders
    """
    base_path = Path(base_path)
    
    if not base_path.exists():
        print(f"Error: Path {base_path} does not exist")
        return
    
    # Get all subdirectories (projects)
    projects = [d for d in base_path.iterdir() if d.is_dir()]
    
    if not projects:
        print(f"No project folders found in {base_path}")
        return
    
    print(f"Found {len(projects)} project(s)\n")
    
    for project in projects:
        print(f"\n{'='*60}")
        print(f"Processing project: {project.name}")
        print(f"{'='*60}")
        
        # Convert PDFs to Markdown
        markdown_files = convert_pdfs_to_markdown(project)
        
        # Generate summary with Ollama
        if markdown_files:
            generate_project_summary(project, markdown_files)
        
        print(f"\nCompleted processing {project.name}")

if __name__ == "__main__":
    # Example usage
    base_path = input("Enter the base path containing project folders: ").strip()
    
    if not base_path:
        base_path = "."  # Use current directory if none provided
    
    process_projects(base_path)
    
    print("\n" + "="*60)
    print("All projects processed!")
    print("="*60)