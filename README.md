# Apex

Sequential 4-payload dropper for FPV drones, driven by a single servo.

Yegor Cherov

<img src="images/assembly-overview.png" alt="Apex full assembly" width="600" />
<img src="images/drone+dropper.jpeg" alt="Apex connected to drone" width="600" />

## Overview

Apex drops up to four independent payloads at separate points in a single 180° servo sweep. There's no onboard electronics beyond the servo itself and no extra FC channels beyond the one driving it.

Payloads attach through zip ties rather than a fixed-geometry bay, so the same hardware handles a wide range of payload shapes and sizes without reprinting.

**Demos**

https://github.com/user-attachments/assets/e3766b08-4272-4210-bcb9-dfcf5e273cf3

V1, SG90 servo, split arm heights.

https://github.com/user-attachments/assets/bb46a15b-bc07-45ec-ad2f-8966f5d29cbe

V2, SG90 servo, unified arm set. The current release (V3) keeps V2's geometry but replaces the servo, see [Version History](#version-history).

## Features

- 4 sequential drops from a single 180° servo sweep
- Single MG996R servo, no added FC channels
- Zip tie payload mounting, works with S and M holders (8 or 4 payload capacity respectively)
- No springs, detents, or secondary latching, the Geneva mechanism holds position on its own
- Base plate bolts to a standard 10" frame pattern, adaptable to other frames in CAD

## Why not an existing design

| Approach | Limitation |
|---|---|
| Single-payload flap/pin release | One drop per flight |
| One servo per payload | Burns FC channels, adds weight and wiring |
| Revolver-style bay | Bay radius is fixed at print time, payload size can't change without a reprint |

Apex targets all of these at once: one servo, multiple sequential drops, and payload geometry that isn't baked into the print.

## How it works

<img src="images/cross-section-full.png" alt="Cross section full view" width="300" />

Four Geneva mechanisms are sequenced along a single driven shaft. One continuous 180° servo rotation trips each mechanism in turn, from the bottom arm to the top.

### Geneva mechanism

A Geneva drive turns continuous rotation into indexed motion. A pin on the driver engages a slotted wheel, rotates it exactly 90°, then disengages; a locking arc on the driver holds the wheel stationary the rest of the time. That gives two things a standard gear can't: a fixed 90° throw per engagement, and a wheel that stays locked in both the open and closed position with no spring or detent needed.

<img src="images/geneva-closeup.png" alt="Geneva engagement detail" width="300" />

### Drop sequence

Four engagement pillars sit on the shaft, spaced 35° apart, one per arm.

| Shaft rotation | Event |
|---|---|
| 0° | First pillar enters first Geneva slot |
| 35° | Arm 1 opens, second pillar engages |
| 70° | Arm 2 opens, third pillar engages |
| 105° | Arm 3 opens, fourth pillar engages |
| 140° | Arm 4 opens |
| 180° | Sweep complete |

The servo holds at 180° after the sweep. Nothing moves again until it's commanded back to reset.

<img src="images/pillar-spacing.png" alt="Pillar spacing detail" width="300" />

### Arm pivot

<img src="images/pyramid-pivot.png" alt="Pyramid pivot socket" width="300" />
<img src="images/pyramid-pivot2.png" alt="Pyramid pivot socket" width="300" />

Cylindrical pins were the first approach and failed under load, the contact area in printed plastic is too small and shears. The current socket uses a pyramid profile instead: wide at the base, narrowing to a rounded tip, with the arm cradled from both above and below. Load spreads across the pyramid face rather than concentrating on a line contact, which held up substantially better in testing.

### Servo and shaft

<img src="images/servo-topdown.png" alt="Servo connection top down" width="300" />
<img src="images/tube-assembly.png" alt="Internal shaft cross section" width="300" />
<img src="images/cross-section-servo.png" alt="Internal shaft cross section" width="300" />

The MG996R sits in the lower housing with its horn coupled directly to the central shaft, which runs the full height of the tube. The shaft splits into two printed parts (Tube Top, Tube Bot) that assemble around the internal structure; the four engagement pillars are molded into the shaft itself.

## Payload holders

<img src="images/payload-holders.png" alt="Payload holders array" width="300" />

| Size | Capacity |
|---|---|
| S | 8 |
| M | 4 |

Each holder has zip tie holes for securing a payload, then slides onto an arm where it's locked in the closed position. Opening the arm 90° via the Geneva drive releases the holder along with the payload. Any payload that can be ziptied to a holder is compatible, there's no fixed bay geometry to work around.

## Specifications

| Parameter | Value |
|---|---|
| Servo | MG996R |
| Operating voltage | 6V, via step-down from drone battery |
| Servo travel | 180° |
| Payload capacity | 4 (M holders) or 8 (S holders) |
| Payload attachment | Zip ties |
| Drive mechanism | 4x Geneva mechanism, single shaft |
| Pillar spacing | ~35° |
| Frame compatibility | 10" bolt pattern (adaptable in CAD) |

## Bill of materials

| Part | Qty | Notes |
|---|---|---|
| MG996R servo | 1 | Or equivalent torque class |
| Step-down converter | 1 | Set to 6V output |
| M2 / M3 / M4 screws | assorted | Servo mount and housing |
| Zip ties | 8-16 per mission | Payload attachment |
| PLA or PETG filament | ~65g | PETG recommended |

## Printing

| Setting | Value |
|---|---|
| Layer height | 0.2mm |
| Infill | 40% minimum |
| Infill pattern | Gyroid or honeycomb |
| Material | PETG preferred, PLA acceptable |
| Supports | Required, arm sockets and servo bay |
| Perimeters | 4 minimum |

The pyramid pivot sockets carry the tightest tolerances in the print. If your printer runs loose, scale the shaft pillars down 1-2% before slicing rather than sanding fit after the fact.

## Assembly

1. Print all parts and clean support material from the pivot sockets and Geneva slots.
2. Seat the MG996R in the lower servo bay.
3. Fit the bottom tube, checking orientation, and secure it to the servo horn with the included screw.
4. Slide the top tube onto the bottom tube and lock with an M3 screw.
5. Fit latch arms 1 and 2 into their sockets.
6. Attach Shell Addition to Shell Main (four M3 screws, both directions); this clamps arms 1 and 2 in place.
7. Fit latch arms 3 and 4 into the remaining sockets.
8. Attach the lid to Shell Addition with four M3 screws to clamp arms 3 and 4.
9. Bolt the base plate to the drone frame (4 mounting holes).
10. Wire per the section below.
11. Bench test a full 180° sweep before flying.
12. Zip tie payloads to holders, slide holders onto arms, and rotate arms closed.

## Wiring

1. Drone battery → step-down converter input
2. Step-down output set to 6V
3. Step-down output → MG996R power/ground
4. MG996R signal → any free servo output on the FC

Do not run the MG996R off the FC's 5V rail directly, it draws enough current under load to brown out the FC or damage the BEC.

### Transmitter setup (RadioMaster)

Map a switch or dial to the servo channel with a 5-point custom curve:

| Point | Output | Position |
|---|---|---|
| 1 | -100% | 0° (armed) |
| 2 | -50% | 35° (drop 1) |
| 3 | 0% | 70° (drop 2) |
| 4 | +50% | 105° (drop 3) |
| 5 | +100% | 140-180° (drop 4) |

Step through points sequentially in flight to release payloads in order.

## Mounting

Base plate bolt pattern matches a Mark4 V2 10" frame. For other frames, edit the base plate in CAD; the housing itself doesn't need to change.

## Version history

| Version | Servo | Change |
|---|---|---|
| V1 | SG90 | First working proof of the Geneva sequencing concept. Split arm geometry (two heights) since all four pillars couldn't sit level. SG90 stalled under load regardless of print tolerance, insufficient torque for a 4-stage sequence. |
| V2 | SG90 | Reworked pillar spacing and shaft diameter so all four pillars sit at one height, enabling a single unified arm set. Kept the SG90 deliberately to isolate the geometry fix; it still stalled, confirming the servo was the bottleneck, not the mechanism. |
| V3 | MG996R | Scaled the whole design up 20% to fit the MG996R, which also improved wall thickness and Geneva slot clearance. No stalls at 6V under payload load. Current release. |

## Known limitations

- Base plate ships sized for a 10" frame; other frame sizes need a CAD edit before printing.
- SG90 is not viable at any print tolerance, this isn't a fit-and-finish issue.
- Payload weight hasn't been formally load-tested past normal FPV payload range; heavy single payloads (500g+) are untested.

## Repository structure

```
3d print/       V3 STL files, ready to print
cad/
  v1/           V1 source
  v2/           V2 source
  v3-final/     V3 source (current)
images/
```

## License

MIT. Use, modify, and redistribute freely. If you improve on it, a pull request or a link back is appreciated.
