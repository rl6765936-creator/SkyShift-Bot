# The SkyShift Technology Platform

**Document ID:** SKS-KB-009
**Version:** 1.6
**Owner:** Office of the CTO
**Last updated:** 30 October 2026

---

## 1. Overview

The **SkyShift platform** is the digital system that runs the SkyShift trial program. It has three parts:

1. **The SkyShift server:** built with **ASP.NET Core on .NET 8**. It holds all the business rules.
2. **The SkyShift web application:** built with **React and TypeScript**. It provides the public site and the participant workspace, and a separate workspace for the operations team.
3. **The database:** **PostgreSQL**, with SQL Server supported as an alternative.

The technical name of the project is **SkyShift**; its business name is **"עולים לאוויר"**.

## 2. Guiding technical principles

1. **The server decides.** Trial dates, eligibility and vehicle availability are calculated only by the server. The web application displays them and never recalculates them.
2. **One winner for every limited resource.** When two requests compete for the same vehicle, exactly one succeeds.
3. **Rules live in one place.** Business rules are written once, in the core of the system, and not repeated elsewhere.
4. **History is never deleted.** Assignments and flights are kept permanently.
5. **Honest data.** Every specification carries an accuracy label.

## 3. Architecture

The server follows **Clean Architecture**: the system is split into layers, and the core business rules do not depend on the database, the web or any external technology.

| Layer | Responsibility |
|---|---|
| **Domain** | The core concepts and their rules: participants, vehicles, vehicle assignments, flights, catalog models, and lottery eligibility |
| **Application** | One clearly defined action per use case, such as registering, selecting a vehicle or recording a flight |
| **Infrastructure** | Storing and reading data safely |
| **API** | Receiving requests from the web application and returning answers |

## 4. The core concepts

| Concept | Main information | Key rules |
|---|---|---|
| **Participant** | Name, email, average daily trips, gender (optional) | Monthly target = average daily trips × 30 |
| **Vehicle** | Status, catalog model, seats, road speed, image, descriptions | Can be assigned only when Available. Retired is final. |
| **Vehicle assignment** | Participant, vehicle, start, end | End = start + exactly one month. Active from start to end, both included. |
| **Flight** | Participant, vehicle, flight date and time, record creation time | Must be within the trial and not in the future. The creation time is set by the server. |
| **Catalog model** | Manufacturer, model, seats, road speed, accuracy labels, image, descriptions | Each catalog model can be used by only one fleet vehicle |

### Lottery eligibility

Eligibility is calculated by a dedicated component of the domain:

- **Threshold:** 80%.
- **Eligibility check:** completed flights × 100 ≥ 80 × expected monthly trips. The comparison uses whole numbers only, so there are no rounding errors.
- **Completion percentage** for display: completed flights × 100 ÷ expected monthly trips, rounded down.
- If the expected monthly trips are 0, the participant is not eligible and the percentage is 0.

**Completed flights** are counted only within the dates of the **active** vehicle assignment.

## 5. Fairness when participants compete

Vehicles are a limited resource. The platform is designed so that **two participants can never hold the same vehicle**, even if they press "select" at exactly the same moment:

- If two participants select the same vehicle at the same time, the first selection to be saved wins. The second participant receives a clear message that the vehicle is no longer available.
- If the same participant sends two selections at the same time, only one assignment is created.
- If a vehicle is being removed from the fleet at the same moment a participant selects it, only one of the two actions succeeds.

These guarantees are covered by automated tests.

## 6. Messages and languages

- The platform is fully available in **Hebrew and English**, including right-to-left layout and gender-appropriate Hebrew addressing.
- Every expected error is returned with a clear message in both languages. The message shown follows the participant's selected language.
- Unexpected errors show a general message, without internal technical details.

## 7. Security and privacy in the platform

- **Passwords** are stored only as secure, one-way hashes. Readable passwords are never stored.
- **Sessions expire** automatically after a period of time; the participant is then asked to sign in again.
- **Permissions are enforced by the server.** Each participant can see only their own data. Management functions are available only to authorized members of the SkyShift operations team, and no one can grant themselves management permissions through the platform.
- **Secret keys** are never stored in the code or in the web application.
- All communication between the browser and the server is encrypted (HTTPS).

## 8. The participant screens

| Screen | Purpose |
|---|---|
| Home | The SkyShift story and animation |
| Sign in / Register | Registration signs the participant in immediately |
| Dashboard | Target, completed flights, completion percentage, eligibility, current vehicle |
| Vehicles | Available fleet, filter by type, select a vehicle |
| My vehicle | The participant's current vehicle and its details |
| Record a flight | Record a completed trip |

The home page animation pauses when it is out of view, has pause and replay controls, and shows a still image for people who prefer reduced motion.

The platform's colour palette uses indigo, lavender, sky blue, turquoise, champagne gold and cream, on mostly light surfaces.

## 9. Management capabilities (summary)

The SkyShift operations team has a separate, protected workspace for running the trial: managing the fleet, following participation, and viewing flights and assignments. Its main indicators are described in SKS-KB-010. The workspace is not available to participants.

## 10. Quality and testing

- The server is covered by automated tests, including tests of vehicle selection under competition, dashboards, vehicle removal rules and error handling, run against real databases.
- The web application is covered by a strict build check and automated browser tests on desktop and mobile layouts.

## 11. Availability

The platform is currently published as a **public demonstration environment**. No vehicles, flights or assignments are created automatically: vehicles are added to the fleet by the operations team.

## 12. Planned technical work

- Verification of flights from trusted vehicle data.
- Automatic return of vehicles to the available pool at the end of a trial.
- The **SkyShift assistant bot**, which answers questions from this knowledge base.
- Flight booking and SkyPad scheduling (for the pilot stage).
