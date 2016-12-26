import requests
import lxml.html


def parse_dev_by(url):
    session = requests.session()
    open_url = session.get(url)

    doc = lxml.html.document_fromstring(open_url.text)

    links = doc.xpath('.//*[@id="tablesort"]/tbody/tr/td[1]/a/@href')
    links_list = [str(a) for a in links]

    total_info = list()

    for link in links_list:
        open_url = session.get('{}{}'.format(url, link))
        doc = lxml.html.document_fromstring(open_url.text)

        email_x = doc.xpath('//div[@class="sidebar-views-contacts h-card vcard"]/ul/li[1]/a')
        email = email_x[0].text

        site_x = doc.xpath('//div[@class="sidebar-views-contacts h-card vcard"]/ul/li[3]/a')
        if str(site_x[0].text).startswith('http'):
            site = str(site_x[0].text)
        else:
            site = 'http://{}'.format(str(site_x[0].text))

        name_x = doc.xpath('//div[@class="widget-companies-header"]/div/div[@class="left"]/h2')
        name = name_x[0].text

        info = dict(name=str(name), site=site, email=str(email))

        total_info.append(info)

    return total_info