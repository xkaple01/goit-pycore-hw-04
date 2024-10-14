import re
from io import BytesIO
from pathlib import Path


file_name_cats: str = 'cats.txt'
path_file_cats: Path = Path(__file__).resolve().parent.joinpath(Path(file_name_cats))

def remove_cats_file(path: Path = path_file_cats) -> None:
    path.unlink(missing_ok=True)

def save_txt(stream: BytesIO, path: Path = path_file_cats) -> None:
    remove_cats_file()
    with open(file=path, mode='wb') as file:
        file.write(stream.getvalue())

def get_cats_info(path: Path = path_file_cats) -> list[dict[str, str]]:
    cats_info: list[dict] = []

    with open(file=path, mode='rt', encoding='UTF-8') as file:
        for line in file:
            split_res: list[str] = line.split(sep=',')

            if len(split_res) != 3:
                raise ValueError('Provided .txt file must contain 3 columns separated with comas.')
            
            id: str = split_res[0]
            name: str = split_res[1]

            if re.fullmatch(pattern='[A-Za-z]{2,20}', string=name) is None:
                raise ValueError('Name must consists only of letters.')
            
            try:
                age: int = int(split_res[2])
            except Exception:
                raise ValueError('Age must be integer number.')
            
            if age < 0 or age > 30:
                raise ValueError('Age must be >= 0 years and <= 30 years.')

            cats_info.append({'id': id, 'name': name, 'age': age})

    return cats_info