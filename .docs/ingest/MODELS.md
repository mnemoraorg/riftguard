# USGS Earthquake Data Models

This document explains the fields used in the `Earthquake` and `Feature` domain models, which map directly to the USGS GeoJSON format. Many of these fields use standard seismological abbreviations.

## Core Properties (`EarthquakeProperties`)

These fields describe the event itself.

| Field         | Type     | Description                                                                                                                                                    |
| :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`mag`**     | `float`  | **Magnitude**. A number that characterizes the relative size of an earthquake. Can be negative for very small events.                                          |
| **`place`**   | `string` | Textual description of the geographic location (e.g., "10km SSW of Idyllwild, CA").                                                                            |
| **`time`**    | `int`    | **Origin Time**. Timestamp (milliseconds since epoch) when the earthquake occurred.                                                                            |
| **`updated`** | `int`    | Timestamp (milliseconds since epoch) when this event was last updated in the catalog.                                                                          |
| **`tz`**      | `int`    | Timezone offset from UTC in minutes at the event location (deprecated/ unreliable).                                                                            |
| **`url`**     | `string` | Link to the USGS Event Page for this specific earthquake.                                                                                                      |
| **`detail`**  | `string` | Link to the full GeoJSON detail feed for this event.                                                                                                           |
| **`status`**  | `string` | Indicates if the event has been reviewed by a human. Values: `automatic` (computer generated), `reviewed` (human verified), `deleted`.                         |
| **`tsunami`** | `int`    | **Tsunami Flag**. `0` = No tsunami expected. `1` = Possible tsunami generated (oceanic events).                                                                |
| **`sig`**     | `int`    | **Significance**. A number from 0-1000 describing how significant the event is, based on magnitude, felt reports, and location. >600 is usually a major event. |
| **`type`**    | `string` | Type of seismic event. Usually `earthquake`, but can be `quarry blast`, `explosion`, `ice quake`, etc.                                                         |
| **`title`**   | `string` | A human-readable title, usually "M [mag] - [place]".                                                                                                           |

## Intensity & Impact

Fields related to how strongly the earthquake was felt.

| Field       | Type     | Description                                                                                                                                                                               |
| :---------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`felt`**  | `int`    | The total number of "Did You Feel It?" reports submitted by the public.                                                                                                                   |
| **`cdi`**   | `float`  | **Community Decimal Intensity**. The maximum reported intensity on the Modified Mercalli Intensity (MMI) scale based on citizen reports. (e.g., 2.5 = barely felt, 7.0 = strong shaking). |
| **`mmi`**   | `float`  | **Modified Mercalli Intensity**. The maximum instrumental intensity calculated from seismic data. This is more scientific than `cdi`.                                                     |
| **`alert`** | `string` | **PAGER Alert Level**. Estimates the impact (fatalities/economic). Values: `green` (low), `yellow`, `orange`, `red` (high impact).                                                        |

## Technical / Seismological Details

Advanced fields mostly useful for scientists.

| Field         | Type     | Description                                                                                                                                                                |
| :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`net`**     | `string` | **Network**. The ID of the seismic network that authored the information (e.g., `us` for USGS, `ci` for Caltech).                                                          |
| **`code`**    | `string` | A unique code assigned by the network (e.g., `123456`).                                                                                                                    |
| **`ids`**     | `string` | Comma-separated list of all event IDs associated with this event (used when multiple networks detect the same event).                                                      |
| **`sources`** | `string` | Comma-separated list of networks that contributed to this event information.                                                                                               |
| **`types`**   | `string` | Comma-separated list of available product types (e.g., `shake-map`, `moment-tensor`).                                                                                      |
| **`nst`**     | `int`    | **Number of Stations**. The total number of seismic stations used to calculate the location. Higher is better.                                                             |
| **`dmin`**    | `float`  | **Distance Minimum**. Horizontal distance from the epicenter to the nearest station (in degrees). Smaller is better (more precise location).                               |
| **`rms`**     | `float`  | **Root Mean Square**. The RMS of the travel time residuals (in seconds). Describes how well the calculated location fits the observed data. Lower (closer to 0) is better. |
| **`gap`**     | `float`  | **Azimuthal Gap**. The largest angle (in degrees) between any two azimuthally adjacent stations. Smaller is better (<180 means stations surround the event).               |
| **`magType`** | `string` | The method used to calculate magnitude (e.g., `ml` (local/Richter), `mw` (moment magnitude), `md` (duration)).                                                             |

## GeoJSON Wrappers (`Feature` & `FeatureCollection`)

These are standard GeoJSON structures.

- **`Feature`**: Represents a single geographic object (the earthquake).
  - `geometry`: Contains the coordinates `[longitude, latitude, depth]`. Note: Depth is in kilometers.
  - `properties`: Contains the `EarthquakeProperties` defined above.
  - `id`: The unique event ID.
- **`FeatureCollection`**: A list of features.
