from selenium.webdriver.common.by import By


class SortablePageLocators:

    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    LIST_ITEM = (By.XPATH, '//div[@class="vertical-list-container mt-4"]//div[@class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GRID_ITEM = (By.XPATH, '//div[@class="grid-container mt-4"]//div[@class="list-group-item list-group-item-action"]')



class SelectablePageLocators:
    LIST_TAB = (By.XPATH, '//a[@id="demo-tab-list"]')
    NOACTIVE_LIST_BUTTONS = (By.XPATH, '//li[@class="mt-2 list-group-item list-group-item-action"]')
    ACTIVE_LIST_BUTTONS = (By.XPATH, '//li[@class="mt-2 list-group-item active list-group-item-action"]')

    GRID_TAB = (By.XPATH, '//a[@id="demo-tab-grid"]')
    ACTIVE_GRID_BUTTONS = (By.XPATH, '//li[@class="list-group-item active list-group-item-action"]')
    NOACTIVE_GRID_BUTTONS = (By.XPATH, '//li[@class="list-group-item list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # Prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    # Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')

class DraggablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')
    # Axis Restricted
    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')
    # ContainerRestrickted
    BOX_TAB = (By.XPATH, '//a[@id="draggableExample-tab-containerRestriction"]')
    WITHIN_THE_BOX = (By.XPATH, '//div[@class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')





