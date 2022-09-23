from pcpartpicker import API
import csv
import moneyed


def writecsv(cards):
    with open('cards.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)

        for card in cards['video-card']:
            if card.price == moneyed.Money('0.00', currency='CAD'):
                continue

            spamwriter.writerow([
                card.brand.strip(),
                card.model,
                card.chipset,
                card.vram.gb,
                # card.core_clock,
                # card.boost_clock,
                # card.color,
                # card.length,
                card.price
            ])

def wrap(elm, str):
    return f'<{elm}>{str}</{elm}>'

def writehtml(cards):
    str = ''

    str += '<html>\n'
    str += '<table>\n'

    for card in cards['video-card']:
        if card.price == moneyed.Money('0.00', currency='CAD'):
            continue

        str += wrap('tr',
                    wrap('td', card.brand) + wrap('td', card.model)
                    + wrap('td', card.chipset) + wrap('td', card.vram.gb) + wrap('td', card.price)

                    )

    str += '</table>\n'
    str += '</html>\n'

    with open('index.html', 'w') as htmlfile:
        htmlfile.write(str)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api = API(region="ca")

    cards = api.retrieve("video-card")

    # writecsv(cards)
    writehtml(cards)
    writecsv(cards)


    # brand: str
    # model: str
    # chipset: str
    # vram: Bytes
    # core_clock: ClockSpeed
    # boost_clock: ClockSpeed
    # color: str
    # length: float
    # price: Money