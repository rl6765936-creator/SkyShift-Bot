# Lottery Regulations: The SkyShift Vehicle Draw

**Document ID:** SKS-KB-005
**Version:** 1.0 (draft, to take effect at the launch of the pilot)
**Owner:** Legal & Operations
**Last updated:** 30 October 2026

---

> **Status notice:** These regulations describe the draw planned for the SkyShift pilot. **No draw is active at this time**, and no prize is being awarded during the demonstration phase. Eligibility shown in the demonstration platform is calculated for illustration only. These regulations will take effect only on the date published when the pilot launches.

## 1. Purpose of the draw

The draw exists to **encourage real, consistent use** of the vehicle during the trial month. SkyShift wants to learn how people would use a personal air vehicle in daily life. The best way to learn this is for participants to actually use it. The draw rewards participants who do.

## 2. Definitions

- **Participant:** a person registered in the SkyShift platform who has accepted the Terms of Participation.
- **Trial month (assignment):** the period from the moment a participant selects a vehicle to exactly one calendar month later, both ends included.
- **Average daily trips:** the whole number the participant declared at registration.
- **Monthly target:** average daily trips × 30.
- **Completed flight:** a flight accepted by the SkyShift platform within the trial month, according to the rules in SKS-KB-004.
- **Completion percentage:** completed flights ÷ monthly target × 100.
- **Eligible participant:** a participant whose completion percentage reached at least 80% within a trial month.
- **Draw cycle:** a defined period, published in advance, at the end of which a draw is held among eligible participants.
- **Experimental vehicle:** a vehicle of the SkyShift fleet designated in the fleet system as a "personal experimental vehicle".

## 3. How to enter the draw

**There is no separate registration for the draw.** A participant enters automatically by meeting the eligibility conditions. Here is the path:

1. **Register** in the SkyShift platform and declare your average daily trips honestly.
2. **Select an available vehicle.** Your one-month trial begins at that moment.
3. **Record every completed flight** in the platform, with the correct local date and time.
4. **Follow your dashboard.** It shows your target, your completed flights and your percentage.
5. **Reach at least 80%** of your monthly target **within the trial month.**
6. When you do, the dashboard shows: "Your participation has met the required threshold." You are now on the list of eligible participants for the draw cycle in which your trial month ended.

## 4. Eligibility conditions

A participant is eligible for a draw cycle if **all** of the following are met:

1. The participant had a trial month that **ended within the draw cycle**.
2. Within that trial month, the participant's completed flights reached **at least 80%** of the monthly target.
3. The participant is aged 18 or over.
4. The participant has accepted the Terms of Participation and has not breached them.
5. The participant is not an employee of SkyShift, a member of the advisory circle, the independent observer, or an immediate family member of any of these.
6. The participant's flight records passed the **integrity review** (section 7).

### How eligibility is calculated

Eligibility is calculated **only by the SkyShift server**, by a fixed rule:

> A participant is eligible when **completed flights × 100 ≥ 80 × monthly target**.

Examples:

- Average 4 trips a day → target 120 → **96 flights** needed.
- Average 2 trips a day → target 60 → **48 flights** needed.
- Average 1 trip a day → target 30 → **24 flights** needed.

Only flights within the trial month count. Flights from earlier or later trial months are not added together.

## 5. The prize

The planned prize in each draw cycle is **the experimental vehicle, at no cost to the winner**, according to the trial terms in force at the time of the draw. The specific vehicle, the terms of transfer or long-term use, and any conditions related to safety, insurance, licensing and regulatory approval will be published before the draw cycle begins.

The prize:

- Is **personal** and cannot be transferred, sold or exchanged for cash.
- Will be delivered only once all regulatory and safety conditions for its use have been met.
- Is subject to the winner completing any training and safety requirements in force at the time.

## 6. How the draw is held

1. **Closing the list.** At the end of each draw cycle, the list of eligible participants is frozen. A participant's place on the list is recorded with an anonymous identifier.
2. **Chances.** Each eligible participant receives **one entry per eligible trial month**. The number of flights above the threshold does not add entries; reaching 80% is what counts.
3. **Random selection.** The winner is chosen by a cryptographically secure random number generator, in a documented procedure.
4. **Supervision.** The draw is held in the presence of an **independent observer** who is not a SkyShift employee. The observer signs a protocol confirming that the draw was held according to these regulations.
5. **Reserve winners.** Two reserve winners are drawn in order, in case the winner does not meet the conditions or does not accept the prize.
6. **Separation of duties.** The platform development team does not take part in holding the draw.

## 7. Integrity review

Because the draw rewards recorded flights, SkyShift reviews the records of eligible participants before the draw. The review checks, among other things:

- That flights were recorded within the trial month and not in the future (these are also enforced automatically by the platform).
- That there are no duplicate records (duplicates at the same date and time are rejected automatically).
- That the pattern of flights is reasonable. For example, a large number of flights recorded within a few minutes may be examined.
- In the pilot stage, that flights match the data recorded by the vehicle itself.

Each flight record keeps two times: the **flight time** reported by the participant, and the **record creation time** set by the server, which the participant cannot change. Both are used in the review.

A participant whose records are found to be false may be removed from the draw and from the trial.

## 8. Notifying the winner

- The winner is notified by email within **14 days** of the draw.
- The winner must confirm acceptance of the prize within **30 days** of notification.
- If the winner does not respond or does not meet the conditions, the prize passes to the first reserve winner, and so on.
- With the winner's consent, SkyShift may publish the winner's first name and town.

## 9. Changes to the regulations

- These regulations do not change in the middle of a draw cycle in a way that harms participants.
- Any change is published at least **30 days** before it takes effect.
- If the draw cannot be held because of circumstances beyond SkyShift's control (for example, a regulatory restriction), SkyShift will publish an update and explain the next steps.

## 10. Questions and appeals

Questions about eligibility or the draw can be sent to **support@skyshift.demo**. A participant who believes their eligibility was calculated incorrectly may request a review within 14 days of the end of the trial month. The review will be completed within 30 days.

## 11. Summary in five lines

1. No separate sign-up: you enter by meeting the threshold.
2. Threshold: 80% of (average daily trips × 30), within your trial month.
3. One entry per eligible trial month.
4. Supervised, random, documented draw.
5. Planned prize: the experimental vehicle at no cost, under the trial terms. No draw is active during the demonstration phase.
