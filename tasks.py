from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Tables import Tables
from RPA.PDF import PDF

@task
def order_robots_from_RobotSpareBIn():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    open_robot_order_website()
    close_annoying_model()
    download_orders_file()

    orders=get_orders()

def open_robot_order_website():
    """Open RobotSpareBin Industries Inc. robot order website"""
    browser.goto("https://robotsparebinindustries.com/#/robot-order")

def close_annoying_model():
    page=browser.page()
    page.click("button:text('OK')")

def download_orders_file():
    """Download orders.csv file from website"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/orders.csv",overwrite=True,target_file="orders.csv")

def get_orders():
    """Read the csv files and return the tables"""
    table = Tables()
    order_table=table.read_table_from_csv("orders.csv")
    print(f"Order Table: {order_table}")
    process_orders(order_table)

def process_orders(orders):
    """Process each of the file from orders.csv"""
    for order in orders:
        print(f"Process Table:{order}")
        fill_the_form(order)



def fill_the_form(order):
    """Fill out the form based on order details"""
    page=browser.page()

    page.select_option("#head",str(order["Head"]))
    page.click(f"//input[@type='radio' and @name='body' and @value={order['Body']} ]")
    page.fill('//*[@class="form-control"][1]',order["Legs"])
    page.fill("#address",order["Address"])
    page.click("button:text('Order')")


