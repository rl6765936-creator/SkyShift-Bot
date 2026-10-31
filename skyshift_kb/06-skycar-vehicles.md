# The SkyCar Vehicle Family

**Document ID:** SKS-KB-006
**Version:** 1.4
**Owner:** Engineering, with the Office of Safety and Airworthiness
**Last updated:** 30 October 2026

---

> **Status notice:** The SkyCar is a **concept vehicle under design**. All performance figures in this document are **design targets**, not measured or certified values. No SkyCar has flown with passengers, and no SkyCar holds an airworthiness certificate. The vehicles shown in the platform catalog are **illustrations** (see SKS-KB-008).

## 1. What is a SkyCar?

The **SkyCar** is SkyShift's concept for a **dual-mode personal vehicle**: on the ground it looks and behaves like a compact electric car, and at a designated take-off point it becomes an electric vertical take-off and landing (eVTOL) aircraft.

The idea behind the SkyCar is the venture's first design principle: **start from the car.** People feel comfortable in a car. They know how to sit in it, load it and travel with family in it. The SkyCar keeps that familiarity and adds a second dimension.

The SkyCar that appears in the animation on the SkyShift home page, lifting off above a queue of cars and continuing above the traffic, is the **SkyCar Five**, the flagship concept of the family.

## 2. The SkyCar family

| Model | Seats | Purpose | Status |
|---|---|---|---|
| **SkyCar Five** | 4 passengers + 1 safety pilot seat | Family and commuter use; flagship concept | Concept design |
| **SkyCar Two** | 1 passenger + 1 safety pilot | Lighter, shorter-range commuter variant | Early concept |

## 3. Two modes, one vehicle

### 3.1 Road mode

In road mode the SkyCar is a compact electric car:

- Electric in-wheel drive on the rear wheels.
- Lift arms and rotors folded and locked inside protected side housings.
- Road speed limited to **100 km/h** in road mode (design target).
- Road mode is used to drive from home to a SkyPad, and from a SkyPad to the final destination.

### 3.2 Air mode

In air mode the SkyCar is an eVTOL aircraft:

- **Eight electric ducted rotors** on four fold-out arms (two rotors per arm, one above the other).
- Vertical take-off, transition to forward flight, and vertical landing.
- Flight only in **approved low-altitude corridors**, between **designated SkyPads**.

### 3.3 Conversion: from road to air

Conversion takes place **only at a SkyPad**, never on a public road. The sequence:

1. The vehicle arrives at the SkyPad in road mode and stops in a marked conversion bay.
2. Automatic system checks run: batteries, rotors, flight computers, sensors, recovery parachute.
3. The arms unfold and lock. Locking is confirmed by independent sensors.
4. The safety pilot and the flight-supervision centre confirm readiness.
5. The vehicle moves to the take-off pad.

Design target for conversion time: **about 90 seconds**, plus the automatic checks.

## 4. Who flies the SkyCar

**The participant does not pilot the SkyCar.** This follows directly from what people told SkyShift in its research: "I don't want to become a pilot."

During the pilot stage:

- Every flight is carried out by a **SkyShift safety pilot**, trained and qualified according to the requirements of the aviation authority.
- The SkyCar's flight-control system is **highly automated**: the safety pilot supervises and can take over at any moment.
- Every flight is monitored in real time by the **SkyShift flight-supervision centre**.

Autonomous flight without a pilot on board is a long-term goal only, and would require separate regulatory approval.

## 5. Design targets: SkyCar Five

All figures below are **design targets** for the concept.

### 5.1 Dimensions and weight

| Item | Design target |
|---|---|
| Length (road mode) | 4.6 m |
| Width (road mode, arms folded) | 2.2 m |
| Width (air mode, arms deployed) | 7.8 m |
| Height | 1.7 m |
| Maximum take-off mass | 1,750 kg |
| Payload (people and luggage) | 450 kg |

### 5.2 Air performance

| Item | Design target |
|---|---|
| Cruise speed | 140 km/h |
| Maximum speed in air mode | 170 km/h |
| Typical flight leg | 15–40 km |
| Maximum range on a single charge | 70 km, **plus** a mandatory energy reserve of 20 minutes of flight |
| Operating altitude | Up to 1,500 ft (about 460 m) above ground, within approved corridors |
| Maximum wind for operations | 25 knots steady, 30 knots gusts (operating limit) |
| Noise | 65 dBA or less at 100 m during cruise |

### 5.3 Energy and charging

| Item | Design target |
|---|---|
| Battery architecture | **Three** independent, electrically isolated battery packs |
| Total energy | 180 kWh |
| Fast charge at a SkyPad (20% → 80%) | About 25 minutes |
| Battery chemistry | Selected for thermal stability; final choice pending testing |

### 5.4 Road performance

| Item | Design target |
|---|---|
| Road speed limit (road mode) | 100 km/h |
| Road range | 150 km |

## 6. Main systems

### 6.1 Distributed electric propulsion

Eight ducted rotors, each driven by its own electric motor and its own motor controller. The ducts protect the rotors, reduce noise and improve efficiency. The SkyCar is designed so that the **loss of any single rotor, motor or controller does not prevent continued safe flight and landing.**

### 6.2 Flight control

- **Fly-by-wire** control: there is no mechanical link between the pilot's controls and the rotors.
- **Three independent flight computers**, each able to fly the vehicle alone, with cross-checking between them.
- Software developed according to the highest design assurance level used in aviation for functions whose failure could be catastrophic.

### 6.3 Navigation and awareness

- Satellite navigation with integrity monitoring, plus inertial navigation that works without satellite signals.
- Radar and optical sensors to detect obstacles and other aircraft.
- **Geofencing**: the flight-control system will not fly outside the approved corridor or into restricted airspace.
- Continuous data link to the flight-supervision centre.

### 6.4 Recovery and protection

- A **whole-vehicle ballistic recovery parachute**, designed to lower the entire SkyCar safely in an extreme emergency.
- Energy-absorbing seats and a protective passenger cell, built on automotive crash-safety principles.
- Battery packs in fire-resistant enclosures, with thermal-runaway containment and venting away from the cabin.

### 6.5 Flight data

Every SkyCar carries a **flight data recorder** that records flight parameters, system status and pilot inputs. In the pilot, flight data will also be used to **automatically verify** participants' recorded flights (see SKS-KB-004 and SKS-KB-013).

## 7. SkyPads: where the SkyCar takes off and lands

A **SkyPad** is a designated, approved take-off and landing site. The SkyCar takes off and lands **only** at SkyPads. Each SkyPad is planned to include:

- One or more take-off and landing pads.
- Conversion bays for road-to-air and air-to-road conversion.
- Fast-charging stations.
- A small waiting area for participants.
- A fire-safety and emergency kit, and trained ground staff.
- A direct link to the flight-supervision centre.

The planned pilot network includes a small number of SkyPads in central Israel, connected by approved corridors. The exact locations will be published only after approval by the relevant authorities.

## 8. A typical journey (planned pilot)

1. The participant books the trip in the app (a future feature) or arrives at the SkyPad by appointment.
2. The participant drives, or is driven, to the SkyPad in road mode.
3. A short safety briefing is given at the first flight; afterwards, a reminder before each flight.
4. Conversion to air mode and automatic checks.
5. Take-off, flight along the approved corridor, landing at the destination SkyPad.
6. Conversion to road mode and continuation of the trip by road.
7. The flight is recorded by the vehicle and appears in the participant's dashboard.

## 9. The SkyCar and the catalog

The SkyShift platform's vehicle catalog shows 22 familiar road-car models with propellers added in the images. These are **illustrations** that convey the dual-mode idea, a car you know with the ability to rise above the traffic. They are **not** SkyCars, and **the road cars shown do not fly**. SkyShift has no connection to the manufacturers of these cars. Details are in SKS-KB-008.

## 10. Environmental profile

- **Zero local emissions** in both modes: fully electric propulsion.
- **Noise:** ducted rotors and a cruise noise target of 65 dBA or less at 100 m.
- **Energy:** SkyShift's goal is for SkyPads to be powered by renewable energy wherever possible.
- **Batteries:** a plan for second-life use and recycling of battery packs at the end of their service in the aircraft.

## 11. What is still open

SkyShift is transparent about the engineering questions still open:

- Final battery chemistry and supplier.
- Detailed design of the folding-arm mechanism and its certification.
- Final noise levels, which can only be confirmed by measurement.
- Final certification basis, which will be agreed with the aviation authority.

Until these are settled, every number in this document remains a design target.
