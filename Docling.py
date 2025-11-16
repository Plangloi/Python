from pathlib import Path
from docling.document_converter import DocumentConverter

# Local PDF path
source = Path("/home/ipat/Documents/Solo Doc/25-01-10 PJCA007334 02_INSTALLATION.pdf")

converter = DocumentConverter()

result = converter.convert(source)

print(result.document.export_to_markdown())
