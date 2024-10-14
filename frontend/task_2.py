import mesop as me
from backend.task_2 import remove_cats_file, save_txt, get_cats_info
from backend.uploader import uploader


@me.stateclass
class State:
    content_provided: bool = False
    exception_message: str = ''
    cats_info: list[dict]

def on_file_upload(e: me.UploadEvent) -> None:
    state: State = me.state(state=State)
    try:
        save_txt(stream=e.file)
        state.cats_info = get_cats_info()
        remove_cats_file()
        state.content_provided = True
    except Exception as ex:
        state.content_provided = False
        state.exception_message = str(ex)

def body_2() -> None:
    with me.box(style=me.Style(padding=me.Padding(top='48px', left='16px'))):
        me.markdown(
            text=(
                '```bash \n'
                'Upload .txt file to explore the cat data. \n \n'
                'File is expected to be in the following format: \n'
                '``` \n'
                '```python \n'
                '60b90c1c13067a15887e1ae1,Tayson,3 \n'
                '0b90c2413067a15887e1ae2,Vika,1 \n'
                '0b90c2e13067a15887e1ae3,Barsik,2 \n'
                '0b90c3b13067a15887e1ae4,Simon,12 \n'
                '0b90c4613067a15887e1ae5,Tessi,5 \n'
                '```'
            )
        )

    with me.box(style=me.Style(text_align='center')):
        uploader(label='Upload .txt file', accepted_file_types=['.txt'], on_upload=on_file_upload, type='stroked')

    state: State = me.state(state=State)

    if state.content_provided:
        with me.box(style=me.Style(display='flex', flex_direction='row', color='gray', padding=me.Padding(top='24px', bottom='16px'))):
            with me.box(style=me.Style(width='33%', text_align='center', font_weight='bold')):
                me.text(text='ID')
            with me.box(style=me.Style(width='33%', text_align='center', font_weight='bold')):
                me.text(text='Name')
            with me.box(style=me.Style(width='33%', text_align='center', font_weight='bold')):
                me.text(text='Age')
        for c in state.cats_info:
            with me.box(style=me.Style(display='flex', flex_direction='row', color='gray')):
                with me.box(style=me.Style(width='33%', text_align='center', padding=me.Padding(bottom='4px'))):
                    me.text(text=f"{c['id']}")
                with me.box(style=me.Style(width='33%', text_align='center', padding=me.Padding(bottom='4px'))):
                    me.text(text=f"{c['name']}")
                with me.box(style=me.Style(width='33%', text_align='center', padding=me.Padding(bottom='4px'))):
                    me.text(text=f"{c['age']}")
    else:
        with me.box(style=me.Style(color='gray', padding=me.Padding(top='32px', bottom='32px', left='16px'))):
           me.text(text=f'{state.exception_message}')
        