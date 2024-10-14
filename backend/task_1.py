import re
from io import BytesIO
from pathlib import Path


file_name_salary: str = 'salary.txt'
path_file_salary: Path = Path(__file__).resolve().parent.joinpath(Path(file_name_salary))

def remove_salary_file(path: Path = path_file_salary) -> None:
    path.unlink(missing_ok=True)

def save_txt(stream: BytesIO, path: Path = path_file_salary) -> None:
    remove_salary_file()
    with open(file=path, mode='wb') as file:
        file.write(stream.getvalue())

def total_salary(path: Path = path_file_salary) -> tuple[float, float]:
    salaries: list[float] = []
    with open(file=path, mode='rt', encoding='UTF-8') as file:
        for line in file:
            split_res: list[str] = line.split(sep=',')

            if len(split_res) != 2:
                raise ValueError('Provided .txt file must contain 2 columns separated with coma.')
            
            name: str = split_res[0]
            
            if re.fullmatch(pattern='[A-Za-z]{2,20} [A-Za-z]{2,20}', string=name) is None:
                raise ValueError('Provided employee name must be in the format: first_name last_name.')

            try:
                salary: float = float(split_res[1])
            except Exception:
                raise ValueError('Salary must be a float number.')
            
            if salary <= 0:
                raise ValueError('Salary must be > 0.')

            salaries.append(salary)

    sum_salary: float = sum(salaries)
    avg_salary: float = round(sum_salary / len(salaries), 2)

    return sum_salary, avg_salary