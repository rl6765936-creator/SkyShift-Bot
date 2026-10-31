# The SkyShift Trial Program

**Document ID:** SKS-KB-004
**Version:** 2.0
**Owner:** Operations & Participant Experience
**Last updated:** 30 October 2026

---

## 1. The idea in one paragraph

In the SkyShift trial, a participant chooses an available vehicle for **one month**, records each completed flight, and follows their progress in a personal workspace. Each participant's monthly target is based on their own travel habits: the **average number of daily trips** they declare at registration, **multiplied by 30**. A participant who completes **at least 80%** of the target within the trial month becomes **eligible for the lottery**, whose planned prize is the experimental vehicle at no cost, according to the trial terms.

> **Status:** The trial program currently runs as a demonstration in the SkyShift platform. The steps below are fully implemented in the platform, but there are no real flights and no active draw at this stage.

## 2. Who can participate

The planned pilot is open to people who meet all of the following:

- Aged 18 or over.
- Hold a valid email address and register in the SkyShift platform.
- Accept the Terms of Participation (SKS-KB-011).
- Complete the SkyShift safety briefing before their first flight (in the pilot stage).
- Are not employees of SkyShift or members of their immediate families (for the lottery; see SKS-KB-005).

In the demonstration phase, anyone can register and try the platform.

## 3. The participant journey, step by step

### Step 1: Register

The participant creates an account with:

| Field | Rules |
|---|---|
| Full name | Required, 1 to 200 characters |
| Email address | Required, valid format, not already registered (letter case does not matter) |
| Password | At least 6 characters |
| Average daily trips | A whole number, at least 1 |
| Gender (optional) | Male or Female; used only to address the participant correctly in Hebrew |

After registration the participant is signed in immediately.

**Why we ask for average daily trips:** this number sets the personal monthly target. A participant who travels 4 times a day has a target of 4 × 30 = **120 trips** per month. A participant who travels twice a day has a target of 60. The target reflects real life, so the trial measures real use.

> Choose your average daily trips honestly. A number that is too high makes the target harder to reach; a number that is too low does not reflect your real travel.

### Step 2: Choose a vehicle

The participant opens the **Vehicles** screen and sees all vehicles currently available in the fleet. Each vehicle card shows the manufacturer and model of the illustration, the number of seats, the maximum road speed, a short description, and an accuracy label for each specification (see SKS-KB-008).

The participant can filter vehicles by type and selects one vehicle. Before confirming, the platform shows:

> "This vehicle will be allocated to you for one month. You can hold one active vehicle assignment at a time."

**Fairness rule: one vehicle, one participant.** Each vehicle can be held by only one participant at a time. If two participants try to select the same vehicle at the same moment, exactly one succeeds. The other receives a clear message that the vehicle is no longer available and is invited to refresh the list and choose another. This is guaranteed by the server (see SKS-KB-009).

**One active vehicle per participant.** A participant who already has an active assignment cannot select a second vehicle.

### Step 3: The trial month begins

When a vehicle is selected, a **vehicle assignment** is created:

- **Start:** the exact moment of selection.
- **End:** exactly one calendar month later (for example, from 14 October at 10:00 to 14 November at 10:00).
- Both the start time and the end time are **included** in the trial period.

The trial dates are set by the server, never by the participant or the interface.

### Step 4: Record flights

After each completed trip, the participant opens **Record a flight** and enters the local date and time of the trip. The platform converts it to universal time (UTC) and sends it to the server. The vehicle is linked to the flight automatically through the active assignment.

A flight is accepted only if all of the following are true:

1. The participant has an **active vehicle assignment**.
2. The date and time are **within the trial month**, including its first and last moments.
3. The date and time are **not in the future**.
4. A flight with **exactly the same date and time** has not already been recorded by the same participant. A duplicate is rejected and **not counted twice**.

When a flight is accepted, the participant sees: "Flight recorded successfully. Your dashboard has been updated."

> In the planned pilot, flights will also be confirmed automatically by data from the vehicle itself. Verification of flights from a trusted vehicle source is planned future work (see SKS-KB-013).

### Step 5: Follow progress in the dashboard

The personal dashboard shows:

| Item | Meaning |
|---|---|
| Current vehicle | The vehicle in the active assignment |
| Trial period | Start and end of the trial month |
| Expected monthly trips | Average daily trips × 30 |
| Completed flights | Flights recorded **within the active trial month** |
| Completion percentage | Completed flights ÷ expected trips × 100, rounded down |
| Lottery eligibility | Calculated by the server: eligible from 80% |

Only flights within the **current** trial month count. Flights from a previous assignment do not carry over.

### Step 6: Reach the threshold

When completed flights reach at least 80% of the target, the dashboard shows:

> "Your participation has met the required threshold."

Until then, it shows: "Eligibility begins at 80% of your expected monthly trips."

## 4. Worked examples

| Average daily trips | Monthly target | 80% threshold | Example result |
|---|---|---|---|
| 1 | 30 | 24 flights | 24 flights → 80% → eligible |
| 2 | 60 | 48 flights | 45 flights → 75% → not yet eligible |
| 3 | 90 | 72 flights | 72 flights → 80% → eligible |
| 4 | 120 | 96 flights | 96 flights → 80% → eligible |
| 5 | 150 | 120 flights | 119 flights → 79% → not yet eligible |

The threshold check uses exact whole-number arithmetic: a participant is eligible when completed flights × 100 is greater than or equal to 80 × the monthly target. There is no rounding in the participant's favour or against them.

## 5. Rules at a glance

1. One participant, one active vehicle.
2. One vehicle, one participant at a time.
3. The trial lasts exactly one month from the moment of selection.
4. Flights count only within the active trial month.
5. No future flights, no flights outside the trial, no duplicates.
6. Target = average daily trips × 30.
7. Eligibility from 80% of the target.
8. The server calculates everything; the interface only displays it.

## 6. What happens at the end of the trial month

When the trial month ends:

- The assignment becomes part of the participant's **assignment history**.
- New flights can no longer be recorded against it.
- The participant's eligibility for that trial month is final, based on flights recorded within it.
- The vehicle is returned to the fleet by the operations team, after inspection, and becomes available again. Automatic return of vehicles at the end of a trial is planned (see SKS-KB-013).

## 7. Common messages and what they mean

| Message | Meaning and what to do |
|---|---|
| "You already have an assigned vehicle." | You have an active trial. Open "My vehicle" to see it. |
| "This vehicle is no longer available." | Someone else selected it first. Refresh the list and choose another. |
| "Select an available vehicle before recording a flight." | You have no active assignment. Choose a vehicle first. |
| "The flight must be within your assigned vehicle's trial period…" | The date you entered is before the start or after the end of your trial month. |
| "A completed flight cannot have a future date or time." | Enter the time of a trip that has already happened. |
| "This flight date and time have already been recorded." | A flight at this exact time already exists; it was not counted twice. |
| "Your session has expired. Please sign in again." | For security, sessions expire. Sign in again. |

## 8. Languages

The platform is available in Hebrew and English. Messages, including error messages, follow the selected language, even when the language is switched after an error has appeared.
