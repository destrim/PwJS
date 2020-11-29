from xml.dom import minidom


def main():
    filepath = r'files/xmlfile.xml'
    xmldoc = minidom.parse(filepath)

    born = xmldoc.createElement("born")
    born.setAttribute("val", "11.11.1974")
    xmldoc.firstChild.appendChild(born)

    xmldoc.getElementsByTagName("lastName")[0].childNodes[0].nodeValue = "DiKarpio"

    with open("files/modifiedxmlfile.xml", "w") as fs:
        fs.write(xmldoc.toxml())
        fs.close()


if __name__ == '__main__':
    main()
