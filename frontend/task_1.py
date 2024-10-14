import mesop as me
from backend.task_1 import path_file_salary, remove_salary_file, save_txt, total_salary
from backend.uploader import uploader


@me.stateclass
class State:
    content_provided: bool = False
    exception_message: str = ''
    salary_sum: float = 0.
    salary_avg: float = 0.
    
def on_file_upload(e: me.UploadEvent) -> None:
    state: State = me.state(state=State)
    try:
        save_txt(stream=e.file)
        state.salary_sum, state.salary_avg = total_salary()
        remove_salary_file()
        state.content_provided = True
    except Exception as ex:
        state.content_provided = False
        state.exception_message = str(ex)

def body_1() -> None:
    with me.box(style=me.Style(padding=me.Padding(top='48px', left='16px'))):
        me.markdown(
            text=(
                '```bash \n'
                'Upload .txt file to compute the total and average salary. \n \n'
                'File is expected to be in the following format: \n'
                '``` \n'
                '```python \n'
                'Alex Korp,3000 \n'
                'Nikita Borisenko,2000 \n'
                'Sitarama Raju,1000 \n'
                '```'
            )
        )

    with me.box(style=me.Style(text_align='center')):
        uploader(label='Upload .txt file', accepted_file_types=['.txt'], on_upload=on_file_upload, type='stroked')

    state: State = me.state(state=State)
    
    if state.content_provided:
        with me.box(style=me.Style(padding=me.Padding(top='24px', bottom='16px', left='16px'))):
            me.markdown(text=f'```bash \nUploaded file path inside container: \n{path_file_salary} \n ```')

        with me.box(style=me.Style(display='flex', flex_direction='row', padding=me.Padding(bottom='16px', left='16px'))):
            with me.box(style=me.Style(display='flex', flex_direction='row', justify_content='center', width='50%')):
                me.text(text=f'Total salary:', style=me.Style(font_weight='bold', color='gray'))
                me.text(text=f'{state.salary_sum}', style=me.Style(color='#54d4ff', padding=me.Padding(left='16px'), font_weight='bold'))
            with me.box(style=me.Style(display='flex', flex_direction='row', justify_content='center', width='50%')):
                me.text(text=f'Average salary:', style=me.Style(font_weight='bold', color='gray'))
                me.text(text=f'{state.salary_avg}', style=me.Style(color='#54d4ff', padding=me.Padding(left='16px'), font_weight='bold'))       
    else:
        with me.box(style=me.Style(color='gray', padding=me.Padding(top='32px', bottom='32px', left='16px'))):
            me.text(text=f'{state.exception_message}')
       