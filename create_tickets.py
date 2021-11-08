#!/usr/bin/env python

from subprocess import run

from pathlib import Path
import json

tickets = []

def create_tickets(show, date, price):

    folder = Path(show)
    folder.mkdir(exist_ok=True)

    for row in range(16):
        for seat in range(16):
            ticket = {
                "title": show,
                "date": date,
                "price": price,
                "row": row,
                "seat": seat,
                "link": f"boydway.com/{show}/{date}/{row}-{seat}"
            }

            json.dump(ticket, open(folder / f"{row}_{seat}.json", "w+"), indent=4)

        tickets.append(
            ticket
        )

    return tickets


create_tickets("Teh_doges", "20/12/21", 500000)

create_tickets("Chals_Hoskninson", "24/12/21", 500000)
