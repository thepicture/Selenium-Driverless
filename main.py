from src.selenium_driverless import webdriver
import asyncio


async def main():
    options = webdriver.ChromeOptions()
    options.user_agent = 'overriden'
    options.add_argument('--headless=new')

    async with webdriver.Chrome(options=options) as driver:
        await driver.get('https://tls.peet.ws/api/all', wait_load=True)
        print(await driver.page_source)


asyncio.run(main())
