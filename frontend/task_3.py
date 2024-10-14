import mesop as me
from backend.task_3 import remove_archive, save_zip, tree, ReportLine
from backend.uploader import uploader


@me.stateclass
class State:
    content_provided: bool = False
    exception_message: str = ''
    archive_structure: list[ReportLine]

def on_file_upload(e: me.UploadEvent) -> None:
    state: State = me.state(state=State)
    try:
        save_zip(stream=e.file)
        state.archive_structure = list(tree())
        remove_archive()
        state.content_provided = True
    except Exception as ex:
        state.content_provided = False
        state.exception_message = str(ex)

def body_3() -> None:
    with me.box(style=me.Style(padding=me.Padding(top='48px', left='16px'))):
        me.markdown(text='```bash \nUpload any .zip file to display the directory structure of uploaded archive. \n ```')

    with me.box(style=me.Style(text_align='center')):
        uploader(label='Upload .zip file', on_upload=on_file_upload, type='stroked')

    state: State = me.state(state=State)

    if state.content_provided:
        with me.box(style=me.Style(padding=me.Padding(top='16px', bottom='8px', left='16px'))):
            with me.box():
                for line in state.archive_structure:
                    me.text(text=line.name, style=me.Style(padding=me.Padding(left=f'{line.padding}px', bottom='4px'), color=line.color, font_weight=line.font_weigth))   
    else:
        with me.box(style=me.Style(padding=me.Padding(top='24px', bottom='24px', left='16px'))):
            me.text(text=state.exception_message, style=me.Style(padding=me.Padding(top='8px', bottom='8px')))
             