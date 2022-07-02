import bs4
from rich.console import Console

import req

console = Console()


def action(start: bool = None, page: bool = True) -> None:
    """_su"""

    if start:
        with open("start_urls.txt", "r", encoding="UTF-8") as file_r:
            urls_read = file_r.read().strip().split()

        reqs = req.Request(urls_read)
        reqs_res = reqs.push()

        for i in reqs_res:
            page_urls(i)

    if page:
        with open("page_urls.txt", "r", encoding="UTF-8") as file_r:
            urls_read = file_r.read().strip().split()

        reqs = req.Request(urls_read)
        reqs_res = reqs.push()

        for i in reqs_res:
            console.print(page_info(i))


def page_urls(page: str) -> None:
    """_su"""

    soup = bs4.BeautifulSoup(page, "lxml")

    urls = soup.find("tbody").find_all("a")

    lst = []

    for i in urls:
        lst.append("https://ark.intel.com/" + i.get("href") + "\n")

    with open("page_urls.txt", "r", encoding="UTF-8") as file_r:
        before = file_r.read()

    with open("page_urls.txt", "w", encoding="UTF-8") as file_w:
        file_w.write(before + "".join(lst))


def page_info(page: str) -> dict[str, dict]:
    """he-he"""

    soup = bs4.BeautifulSoup(page, "lxml")

    temp_naming = soup.find("div", class_="product-family-title-text")
    cpu_name = temp_naming.find("h1").text.strip()
    cpu_mini = temp_naming.find("div").text.strip()

    soup_block = soup.find("div", {"id": "tab-blade-1-0"})

    titles = [
        i.find("h2").text.strip() for i in soup_block.find_all("div", class_="subhead")
    ]

    dct = {}
    for i in titles:
        temp = soup_block.find(
            "h2", text=i
        ).next_element.next_element.next_element.next_element
        dct[i] = dict(
            zip(
                map(lambda x: x.text.strip(), temp.find_all("span", class_="label")),
                map(lambda x: x.text.strip(), temp.find_all("span", class_="value")),
            )
        )

    return {f"{cpu_name}({cpu_mini})": dct}


def main() -> None:
    """__s"""

    return action()


if __name__ == "__main__":
    main()
