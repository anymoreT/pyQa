from .TextInput import TextInputElement
from .Select import SelectElement
from .Text import TextElement
from .Button import ButtonElement
from .Link import LinkElement
from .CheckBox import CheckBoxElement
from .Table import TableElement
from .RadioButton import RadioButtonElement
from .FileTextInput import FileTextInputElement
from  .WebElement import WebElement


'''
    locator : ("xpath", "//input[@type='file']")
    locator : ("xpath", "//input[@type='%d']/[%s]/[%d]")
    使用PageEelemnt方式，直接通过定义页面元素集合，在页面直接调用元素，方便case直接使用
    class PageLocator(object):
        H5Text = ("xpath", "//input[@type='file']")
        H6Text = ("xpath", "//input[@type='%d']/[%s]/[%d]")
'''
class PageNormalElement(WebElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            WebElement.__init__(self, locator[0], locator[1])
        else:
            WebElement.__init__(self, locator[0], locator[1] % (property))


class PageTextInputElement(TextInputElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            TextInputElement.__init__(self, locator[0], locator[1])
        else:
            TextInputElement.__init__(self, locator[0], locator[1] % (property))

class PageSelectElement(SelectElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            SelectElement.__init__(self, locator[0], locator[1])
        else:
            SelectElement.__init__(self, locator[0], locator[1] % (property))


class PageTextElement(TextElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            TextElement.__init__(self, locator[0], locator[1])
        else:
            TextElement.__init__(self, locator[0], locator[1] % (property))


class PageButtonElement(ButtonElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            ButtonElement.__init__(self, locator[0], locator[1])
        else:
            ButtonElement.__init__(self, locator[0], locator[1] % (property))

class PageLinkElement(LinkElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            LinkElement.__init__(self, locator[0], locator[1])
        else:
            LinkElement.__init__(self, locator[0], locator[1] % (property))

class PageCheckBoxElement(CheckBoxElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            CheckBoxElement.__init__(self, locator[0], locator[1])
        else:
            CheckBoxElement.__init__(self, locator[0], locator[1] % (property))


class PageTableElement(TableElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            TableElement.__init__(self, locator[0], locator[1])
        else:
            TableElement.__init__(self, locator[0], locator[1] % (property))

class PageRadioButtonElement(RadioButtonElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            RadioButtonElement.__init__(self, locator[0], locator[1])
        else:
            RadioButtonElement.__init__(self, locator[0], locator[1] % (property))


class PageFileTextInputElement(FileTextInputElement):
    def __init__(self, locator, *property):
        if len(property) == 0:
            FileTextInputElement.__init__(self, locator[0], locator[1])
        else:
            FileTextInputElement.__init__(self, locator[0], locator[1] % (property))

