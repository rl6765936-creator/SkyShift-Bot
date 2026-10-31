# The Fleet and the Vehicle Catalog

**Document ID:** SKS-KB-008
**Version:** 1.1
**Owner:** Operations (Fleet), with Engineering
**Last updated:** 30 October 2026

---

## 1. Catalog and fleet: two different things

The SkyShift platform separates two concepts:

- **The catalog** is the list of **vehicle models** that the fleet can be built from. It contains **22 models**. Each catalog model has a manufacturer, a model name, a number of seats, a maximum road speed, an image, and short descriptions in English and Hebrew.
- **The fleet** is the set of **actual vehicles** that participants can select. A Manager creates a fleet vehicle by choosing a catalog model. Each catalog model can be used for **only one** fleet vehicle at a time.

When a Manager creates a vehicle, its details (manufacturer, model, road speed, seats, description) are **filled in automatically from the catalog and locked**. They cannot be edited by hand, so the information shown to participants is always consistent with the catalog.

## 2. The most important thing to know about the catalog images

> **Every catalog image is an edited picture of a road car with added propellers. No road car in the catalog can fly.**

The images are **illustrations** of SkyShift's idea, a familiar car that can rise above the traffic. They are **not** SkyCars (SKS-KB-006), and they are **not** products of SkyShift. SkyShift has **no connection** to the manufacturers of these cars, and the manufacturers have not approved or endorsed SkyShift in any way. Every vehicle card in the platform states:

> "Propellers are a SkyShift illustration; the road car does not fly."

SkyShift stores **no flight specifications** for catalog vehicles. The only specifications stored are **seats** and **maximum road speed**.

## 3. Accuracy labels

Every specification in the catalog carries its own **accuracy label**:

| Label | Meaning |
|---|---|
| **Manufacturer specification** (Verified) | Taken from an official manufacturer document |
| **Illustrative** | A plausible SkyShift sample value. **Not** a manufacturer specification |

Separately, each model carries an **identification label**:

| Label | Meaning |
|---|---|
| **Identified** | The manufacturer and model in the image have been identified with reasonable confidence |
| **Visual inspiration** | The exact model is not verified; the image serves as visual inspiration only. Such models carry only illustrative figures |

Identification and accuracy are separate: a correctly identified car can still have illustrative figures. Concept cars and camouflaged prototypes have no production specifications, so their figures are illustrative.

## 4. The 22 catalog models

| # | Manufacturer and model (illustration) | Identification | Seats | Max road speed (km/h) |
|---|---|---|---|---|
| 1 | Audi Q3 (2nd generation) | Identified | 5 (Illustrative) | 210 (Illustrative) |
| 2 | Geely Geometry E (uncertain) | Visual inspiration | 5 (Illustrative) | 150 (Illustrative) |
| 3 | Koenigsegg Regera | Identified | 2 (Illustrative) | 400 (Illustrative) |
| 4 | Bugatti Chiron Super Sport | Identified | 2 (Illustrative) | 440 (Verified, electronically limited) |
| 5 | Tesla Model X | Identified | 5 (Illustrative) | 250 (Illustrative) |
| 6 | BMW i Vision Circular (concept) | Identified | 4 (Verified) | 180 (Illustrative) |
| 7 | Mercedes-Benz CLE Coupé prototype (uncertain) | Visual inspiration | 4 (Illustrative) | 250 (Illustrative) |
| 8 | Mercedes-Benz Concept CLA Class (concept) | Identified | 5 (Illustrative) | 210 (Illustrative) |
| 9 | Nissan N7 | Identified | 5 (Illustrative) | 170 (Illustrative) |
| 10 | BMW Vision Neue Klasse (concept) | Identified | 5 (Illustrative) | 200 (Illustrative) |
| 11 | BMW 5 Series (G30, art livery) | Identified | 5 (Illustrative) | 250 (Illustrative) |
| 12 | Lancia Pu+Ra HPE (concept) | Identified | 4 (Illustrative) | 180 (Illustrative) |
| 13 | Bestune Xiaoma (uncertain) | Visual inspiration | 4 (Illustrative) | 100 (Illustrative) |
| 14 | Toyota Prius Plug-in Hybrid (5th generation) | Identified | 5 (Illustrative) | 175 (Illustrative) |
| 15 | Škoda Kodiaq (2nd generation, prototype) | Identified | 5 (Illustrative) | 200 (Illustrative) |
| 16 | Maserati GranCabrio (prototype) | Identified | 4 (Illustrative) | 300 (Illustrative) |
| 17 | Unidentified hypercar | Visual inspiration | 2 (Illustrative) | 350 (Illustrative) |
| 18 | Mercedes-Benz EQB | Identified | 5 (Illustrative) | 160 (Illustrative) |
| 19 | MINI Countryman (3rd generation, prototype) | Identified | 5 (Verified) | 210 (Illustrative) |
| 20 | Chery QQ Ice Cream | Identified | 4 (Illustrative) | 100 (Illustrative) |
| 21 | MINI Cooper E (3-door) | Identified | 4 (Verified) | 160 (Verified) |
| 22 | Peugeot E-3008 | Identified | 5 (Illustrative) | 170 (Illustrative) |

**Summary of accuracy:** seats are verified for 3 models (6, 19, 21) and illustrative for 19. Maximum road speed is verified for 2 models (4, 21) and illustrative for 20.

### Sources of verified values

| Model | Verified value | Source |
|---|---|---|
| Bugatti Chiron Super Sport | Road top speed 440 km/h, electronically limited | Bugatti newsroom |
| BMW i Vision Circular | 4 seats | BMW Group PressClub, September 2021 |
| MINI Countryman | 5 seats | BMW Group PressClub technical specifications, March 2024 |
| MINI Cooper E | 4 seats, road top speed 160 km/h | BMW Group PressClub technical specifications, November 2023 |

The MINI Countryman's road speed differs between official documents for different variants, so it is stored as illustrative.

### How an illustrative value becomes verified

To change a value to "Verified", the seats and road top speed are taken from **one** official document for **one** specific variant, and the catalog row is updated in a dedicated, reviewed database change.

## 5. Fleet vehicle statuses

Each fleet vehicle has exactly one status at any time:

| Status | Meaning | Can a participant select it? |
|---|---|---|
| **Available** | Ready for a new trial | Yes |
| **In use** | Assigned to a participant in an active trial | No |
| **Maintenance** | Undergoing inspection or maintenance | No |
| **Unavailable** | Temporarily out of service for another reason | No |
| **Retired** | Permanently removed from the active fleet | No (final status) |

### Status rules

- A new vehicle always starts as **Available**.
- Only a **participant's selection** moves a vehicle from Available to **In use**.
- While a vehicle is **In use**, a Manager **cannot** change its status.
- **Retired** is final: a retired vehicle cannot return to any other status.
- From Available, Maintenance or Unavailable, a Manager may move a vehicle to Available, Maintenance, Unavailable or Retired.
- There is no "free" status setter; each change is a separate, checked action.

## 6. Personal experimental vehicles

When creating a fleet vehicle, a Manager can mark it as a **"personal experimental vehicle"**. This marks the vehicle as part of the group of experimental vehicles designated for personal trial use, from which the lottery prize vehicle is planned to come (see SKS-KB-005).

## 7. Deleting a fleet vehicle

A Manager can delete a fleet vehicle **only** if:

- It is **Available**, and
- It has **never** had an assignment or a recorded flight.

A vehicle with history is never deleted, because history (assignments and flights) must be preserved. Such a vehicle should be **retired** instead. When an unused vehicle is deleted, its catalog model becomes available again for creating a new fleet vehicle.

## 8. What participants see on a vehicle card

- Manufacturer and model (of the illustration).
- Number of seats, with its accuracy label.
- Maximum road speed, with its accuracy label.
- A note if the model is visual inspiration only.
- Short description, in the selected language.
- The notice: "Propellers are a SkyShift illustration; the road car does not fly."

Vehicles without catalog specifications show a general illustration.

## 9. Optional future catalog additions

The SkyShift image library contains additional vehicles that are not yet in the catalog. Adding a model requires a prepared image, a specification check and a reviewed database change. Until then, they are not part of the catalog and cannot be added to the fleet.
