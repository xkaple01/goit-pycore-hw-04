import mesop as me
from typing import Callable

from frontend.task_1 import body_1
from frontend.task_2 import body_2
from frontend.task_3 import body_3
from frontend.task_4 import body_4


security_policy = me.SecurityPolicy(dangerously_disable_trusted_types=True)

def on_load_page(e: me.LoadEvent) -> None:
    me.set_theme_mode(theme_mode='dark')

@me.page(path='/', title='Main', on_load=lambda e: me.set_theme_mode(theme_mode='dark'), security_policy=security_policy)
def page_main() -> None:
    page_base(body=body_4)

@me.page(path='/task_1', title='Task 1', on_load=lambda e: me.set_theme_mode(theme_mode='dark'), security_policy=security_policy)
def page_task_1() -> None:
    page_base(body=body_1)

@me.page(path='/task_2', title='Task 2', on_load=lambda e: me.set_theme_mode(theme_mode='dark'), security_policy=security_policy)
def page_task_2() -> None:
    page_base(body=body_2)

@me.page(path='/task_3', title='Task 3', on_load=lambda e: me.set_theme_mode(theme_mode='dark'), security_policy=security_policy)
def page_task_3() -> None:
    page_base(body=body_3)

@me.page(path='/task_4', title='Task 4', on_load=lambda e: me.set_theme_mode(theme_mode='dark'), security_policy=security_policy)
def page_task_4() -> None:
    page_base(body=body_4)

def header() -> None:
    with me.box(
        style=me.Style(
            display='flex', flex_direction='row', text_align='center', border_radius=8,
            border=me.Border(bottom=me.BorderSide(width=1, color='white', style='solid'))
        )
    ):
        with me.box(style=me.Style(width='25%')):
            me.button(label='Task 1', on_click=lambda e: me.navigate(url='/task_1'))
        with me.box(style=me.Style(width='25%')):
            me.button(label='Task 2', on_click=lambda e: me.navigate(url='/task_2'))
        with me.box(style=me.Style(width='25%')):
            me.button(label='Task 3', on_click=lambda e: me.navigate(url='/task_3'))
        with me.box(style=me.Style(width='25%')):
            me.button(label='Task 4', on_click=lambda e: me.navigate(url='/task_4'))

def footer() -> None:
    me.box(style=me.Style(height='16px'))

def page_base(body: Callable[[None], None]) -> None:
    with me.box(style=me.Style(width='100%', height='100%')):
        with me.box(
            style=me.Style(
                width='720px', justify_self='center', border_radius='8px', font_family='Roboto', font_size=14,
                border=me.Border.all(value=me.BorderSide(width=1, color='white', style='solid'))
            )
        ):
            header()
            body()
            footer()
        
