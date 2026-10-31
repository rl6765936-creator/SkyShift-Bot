# Safety Standards and the SkyShift Safety Framework

**Document ID:** SKS-KB-007
**Version:** SSF 1.2
**Owner:** Office of Safety and Airworthiness (Chief Safety and Airworthiness Officer)
**Last updated:** 30 October 2026

---

> **Status notice:** SkyShift currently carries out no flights. The SkyShift Safety Framework (SSF) defines the requirements that every SkyCar, every SkyPad and every flight must meet **before** any flight takes place. Alignment with international standards described here is a **design commitment**, not a certification. Only an aviation authority can certify an aircraft.

## 1. Safety philosophy

SkyShift's safety philosophy fits in one sentence:

**"A single failure must never be allowed to become a catastrophe."**

Four principles follow from it:

1. **Safety before everything.** No schedule, budget or publicity goal justifies a flight that is not safe.
2. **Redundancy everywhere it matters.** Every system whose failure could endanger people has at least one independent backup.
3. **The strictest relevant standard.** When there is a choice between standards, SkyShift designs to the stricter one.
4. **Independent authority to stop.** The Chief Safety and Airworthiness Officer may stop any activity, and commercial considerations cannot override the stop.

## 2. The international standards SkyShift aligns with

### 2.1 EASA Special Condition for VTOL aircraft (SC-VTOL)

In July 2019 the European Union Aviation Safety Agency (EASA) published its Special Condition for small-category VTOL aircraft (SC-VTOL-01). It defines two categories:

- **Basic:** for lower-risk, non-commercial operations.
- **Enhanced:** for operations over congested areas or commercial passenger transport.

In the **Enhanced** category:

- The aircraft must be able to **continue safe flight and landing** after a failure, and reach its destination or an alternate landing site.
- A **single failure must not have a catastrophic effect**.
- Catastrophic failure conditions must be **extremely improbable**, with a quantitative objective of no more than **one in a billion per flight hour (10⁻⁹)**, the same level of safety required of large commercial airliners.

**SkyShift's commitment:** the SkyCar is designed to the requirements of the **Enhanced** category, even for the pilot stage, because the SkyCar is intended to carry passengers near populated areas.

### 2.2 FAA powered-lift rules

On 22 October 2024 the United States FAA issued a final rule and a Special Federal Aviation Regulation (SFAR) for **powered-lift** aircraft, the category to which most eVTOL aircraft belong. The rule covers the qualifications and training of pilots and instructors, and operational requirements for this category.

**SkyShift's commitment:** the training program for SkyShift safety pilots is designed to be at least as demanding as the approach in this framework, including training in full-flight simulators and type-specific training on the SkyCar. In Israel, the requirements of the Civil Aviation Authority of Israel are binding and take precedence.

### 2.3 Israeli regulation

Any flight in Israel requires the approvals of the **Civil Aviation Authority of Israel (CAAI)** and coordination with all relevant airspace authorities. SkyShift will carry out no flight without all required approvals. Israel's National Drone Initiative (INDI), led by government bodies including the Ministry of Transport, the Israel Innovation Authority, Ayalon Highways and the CAAI, has been running experiments with drones and air taxis since 2019. SkyShift is **not** part of INDI, but follows the regulatory knowledge developing in Israel closely.

### 2.4 Automotive safety in road mode

In road mode the SkyCar is a road vehicle and must meet the road-vehicle safety requirements that apply to it, including crash protection, lighting, braking and road-approval requirements.

## 3. Safety targets of the SkyShift Safety Framework

| Failure classification | Effect | SkyShift target (per flight hour) |
|---|---|---|
| Catastrophic | Loss of continued safe flight and landing | ≤ 10⁻⁹, and never from a single failure |
| Hazardous | Serious injury possible; large reduction in safety margins | ≤ 10⁻⁷ |
| Major | Significant reduction in safety margins; possible discomfort | ≤ 10⁻⁵ |
| Minor | Slight reduction in safety margins | ≤ 10⁻³ |
| No safety effect | — | No requirement |

Every system is analysed with a formal **system safety assessment**: a functional hazard assessment, fault-tree analysis and failure-mode analysis. Each analysis is reviewed by the Office of Safety and Airworthiness.

## 4. Redundancy: the layers of protection

| System | Redundancy in the SkyCar design |
|---|---|
| Propulsion | 8 rotors, each with its own motor and controller; designed to continue safe flight after losing any one |
| Energy | 3 independent, electrically isolated battery packs; loss of one pack still allows a safe landing |
| Flight control | 3 independent flight computers, each able to fly alone, with cross-checking |
| Navigation | Satellite navigation with integrity monitoring, plus independent inertial navigation |
| Communication | Two independent data links to the flight-supervision centre, plus voice radio |
| Human | A trained safety pilot on board, plus monitoring from the flight-supervision centre |
| Last resort | A whole-vehicle ballistic recovery parachute |

## 5. Operational safety rules

### 5.1 Before every flight

- Automatic system check: batteries, rotors, flight computers, sensors, parachute.
- Visual inspection by ground staff according to a checklist.
- Confirmation that arms are unfolded and locked, by independent sensors.
- Weather check against operating limits.
- Confirmation of the energy plan: the flight leg **plus** a 20-minute reserve.
- Confirmation of the passengers' weight and seating against the vehicle's limits.
- Safety briefing for the passengers (full briefing at the first flight; reminder afterwards).

### 5.2 Weather limits (operating rules)

- No flight in thunderstorms or in forecast thunderstorm conditions.
- Steady wind up to 25 knots, gusts up to 30 knots.
- Daytime flights in visual conditions only during the first stage of the pilot.
- No flight in icing conditions.

### 5.3 Where the SkyCar may fly

- Only between approved SkyPads.
- Only within approved corridors and up to the approved altitude.
- Geofencing in the flight-control system prevents departure from the corridor.

### 5.4 Passengers

- Participants are passengers only; they do not operate the aircraft.
- Seat belts must be fastened from conversion until the end of air-to-road conversion.
- Dangerous goods may not be carried.
- A passenger who feels unwell may ask to cancel or end the flight at the nearest safe point.

## 6. Emergency procedures (summary)

| Situation | Planned response |
|---|---|
| Loss of one rotor or motor | Automatic redistribution of thrust; continue to the destination or nearest SkyPad |
| Loss of one battery pack | Isolation of the pack; landing at the nearest SkyPad |
| Flight-computer disagreement | Automatic exclusion of the faulty computer; continue on the remaining computers |
| Loss of data link | Switch to the backup link; if both are lost, the vehicle follows a pre-programmed safe route to landing |
| Battery thermal event | Isolation, containment, venting away from the cabin; immediate landing |
| Extreme emergency | Deployment of the whole-vehicle recovery parachute |

## 7. Maintenance and fleet status

Safety continues on the ground:

- Every SkyCar has a **maintenance programme** with inspections based on flight hours, cycles and calendar time.
- A vehicle that needs maintenance is moved to **"Maintenance"** status in the SkyShift fleet system. While in this status it cannot be assigned to participants.
- A vehicle that is temporarily unusable for another reason is moved to **"Unavailable"**.
- A vehicle permanently removed from service is moved to **"Retired"**. This status is final.
- A vehicle that is in use by a participant cannot be moved to another status until its assignment ends.

More detail on fleet statuses is in SKS-KB-008 and SKS-KB-010.

## 8. Safety reporting culture

SkyShift encourages everyone to report any safety concern, near-miss or mistake. Reports can be sent to **safety@skyshift.demo**.

- Reports are handled confidentially.
- SkyShift operates a **just culture**: a person who reports an honest mistake will not be punished for reporting it. The goal is to learn and prevent recurrence.
- Every report receives a response, and lessons learned are shared with the whole team.

## 9. Safety pilots

SkyShift safety pilots:

- Hold the pilot licences and ratings required by the aviation authority.
- Complete SkyCar type-specific training, including simulator training of emergency procedures.
- Undergo recurrent training and checks at fixed intervals.
- Are subject to rest-time and fitness-for-duty rules.

## 10. Safety of people on the ground

- Corridors are planned to avoid flying directly over crowded places wherever possible.
- SkyPads are planned with safety zones around the pads.
- Noise is monitored, and complaints from residents are investigated.

## 11. Safety in the digital platform

Safety also means reliable data:

- Vehicle status is controlled only by authorized Managers, with fixed transition rules.
- The platform does not allow a vehicle to be assigned to two participants at the same time.
- Flight records are protected against duplicates and against future or out-of-trial dates.

## 12. Summary

| Question | Answer |
|---|---|
| Which standard does the SkyCar aim for? | The Enhanced category of EASA's SC-VTOL, 10⁻⁹ per flight hour for catastrophic failures |
| Who flies the SkyCar? | A trained SkyShift safety pilot, with monitoring from the flight-supervision centre |
| Can a single failure cause a crash? | The design requirement is that no single failure may be catastrophic |
| Is there a parachute? | Yes, a whole-vehicle ballistic recovery parachute is part of the design |
| Is the SkyCar certified? | No. It is a concept; certification will be sought from the aviation authority |
| Are flights taking place today? | No. No flight will take place before every safety and regulatory requirement is met |
