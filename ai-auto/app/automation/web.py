from playwright.async_api import async_playwright

class WebAutomator:
    def __init__(self):
        self.pw = None
        self.browser = None
        self.context = None
        self.page = None
        self._started = False

    async def start(self):
        if not self._started:
            self.pw = await async_playwright().start()
            self.browser = await self.pw.chromium.launch(headless=True)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()
            self._started = True

    async def go_to(self, url: str) -> str:
        await self.start()
        await self.page.goto(url, wait_until="domcontentloaded", timeout=20000)
        return (await self.page.inner_text("body"))[:3000]

    async def click(self, selector: str) -> str:
        await self.start()
        await self.page.click(selector, timeout=10000)
        await self.page.wait_for_load_state("domcontentloaded")
        return f"Clickeado en '{selector}'. Texto actual: " + (await self.page.inner_text("body"))[:2000]

    async def type_text(self, selector: str, text: str) -> str:
        await self.start()
        await self.page.fill(selector, text, timeout=10000)
        return f"Escrito '{text}' en '{selector}'"

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.pw:
            await self.pw.stop()

# Instancia global (pero no se inicia hasta que se llama a un método)
automator = WebAutomator()