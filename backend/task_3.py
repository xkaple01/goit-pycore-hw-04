import shutil
from io import BytesIO
from pathlib import Path
from collections.abc import Generator
from dataclasses import dataclass


zip_name: str = 'archive.zip'
folder_name: str = 'archive'
path_backend: Path = Path(__file__).resolve().parent
path_zip: Path = path_backend.joinpath(Path(zip_name))
path_dir: Path = path_backend.joinpath(Path(folder_name))

def remove_archive(path_zip: Path = path_zip, path_dir: Path = path_dir) -> None:
    path_zip.unlink(missing_ok=True)
    shutil.rmtree(path=path_dir, ignore_errors=True)

def unpack_archive(path_zip: Path = path_zip, path_dir: Path = path_dir) -> None:
    shutil.unpack_archive(filename=path_zip, extract_dir=path_dir)

def save_zip(stream: BytesIO, path_zip: Path = path_zip, path_dir: Path = path_dir) -> None:
    remove_archive(path_zip=path_zip, path_dir=path_dir)
    with open(file=path_zip, mode='wb') as file:
        file.write(stream.getvalue())
    unpack_archive(path_zip=path_zip, path_dir=path_dir)
    
@dataclass
class ReportLine:
    padding: int = 0
    name: str = ''
    color: str = ''
    font_weigth: str = ''

def tree(path_dir: Path = path_dir, padding: int = 0) -> Generator[ReportLine]: 
    contents = list(path_dir.iterdir())
    for path in contents:
        if path.is_dir():
            yield ReportLine(padding=padding, name=path.name, color='#54d4ff', font_weigth='bold')
            yield from tree(path, padding=padding+16)
        else:
            yield ReportLine(padding=padding, name=path.name, color='gray', font_weigth='medium')