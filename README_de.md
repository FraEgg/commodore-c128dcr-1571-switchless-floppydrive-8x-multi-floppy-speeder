# Switchless 8x Multi-Floppy-Speeder mit 32 KB RAM-Erweiterung für den Commodore C128 DCR und das interne 1571-Diskettenlaufwerk (DolphinDOS 3 kompatibel)

<img title="8x Multi-Floppy-Speeder 32KB RAM Expasion for the internal 1571 Floppydrive C128DCR - DolphinDos 3" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0_C128DCR_Multi-Floppy-Speeder-Set-Title.jpg" alt="loading-ag-1227" data-align="center" style="zoom:25%;">

## Beschreibung

Dieses Projekt ist eine Weiterentwicklung des sehr schnellen und beliebten DolphinDos3 für den C128 und dem 1571 Diskettenlaufwerk. Es nutzt das beste aus der Retro-Welt und der Technik der Gegenwart und war bisher so noch nie verfügbar. Switchless 8x Multi-Floppy-Speeder läuft nicht nur mit DolphinDos 3 sondern es können bis zu 8x DOS Kernals und C128/C64  Kernals betrieben und komfortabel per DOS-Kommandos aktiviert werden. Somit kann neben dem originalen CBM-Dos und DolphinDos 3 z.B. auch JiffyDOS 128 betrieben werden. Das sorgt für maximale Kompatibilität. Die 32KB RAM Erweiterung wird in 4x 8KB Bänken organisiert und ermöglicht zusammen mit dem Peripheral Interface Adapter (PIA, Typ 6821 oder 6521) eine ultraschnelle parallel Datenübertragung und Steuerung der 4x 8K RAM-Bänke (32KB).

Der Switchless 8x Multi-Floppy-Speeder mit 32 KB RAM-Erweiterung für den Commodore C128DCR ist einer der universell einsetzbaren Beschleuniger für das interne 1571-Diskettenlaufwerk des C128DCR. 

Zudem ist der "Switchless 8x Multi-Floppy-Speeder" vollständig RAMBoard-kompatibel, was den Einsatz entsprechender Nibble-Kopierprogramme, die RAMBoard unterstützen, ermöglicht.

## Funktionen

1. 8 x 64 KB ROM-Bänke für C128/C64-Kernals
2. 8 x 64 KB ROM-Bänke für das interne 1571-Diskettenlaufwerk
3. 32 KB RAM-Erweiterung für das 1571-Diskettenlaufwerk** (4 Bänke, schaltbar über PIA)
4. Parallelport für das 1571-Diskettenlaufwerk** (PIA 6821)
5. U32-Kernal-Adapter-Sockel für die C128/C64 8x-Kernal-Umschaltung (Switchless)
6. U4 6526-CIA-Adapter für den Parallelport des internen 1571-Diskettenlaufwerks
7. Kompatibilität mit RAMBoard für Nibbler-Kopierprogramme
   
   

## Benchmark

Hier habe ich einige Benchmarks mit dem 8x Multi-Speeder 32KB RAM erstellt > [[hier]](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/blob/main/benchmark/README.md)

## Funktionsweise

Der Switchless 8x Multi-Floppy-Speeder" für den Commodore C128DCR basiert auf der Weiterentwicklung des 8x Multi-Floppy-Speeders für das 1541-Diskettenlaufwerk. In einem 512 KB EPROM (27C040 oder 29F040) können bis zu acht Kernal-Betriebssysteme für das 1571-Diskettenlaufwerk gespeichert werden. Ein Peripheral Interface Adapter (PIA, Typ 6821 oder 6521) erweitert das Diskettenlaufwerk um einen 8-Bit-Parallelport.

Zusammen mit der 32 KB RAM-Erweiterung (SRAM 62256) ist es möglich, Dolphin DOS 3 zu betreiben. Dadurch kann das Laufwerk komplette Tracks in einem Durchgang einlesen, was beispielsweise das Laden von Programmen im Dolphin DOS 3-Modus im C128 und im C64-Betrieb um den Faktor 38 beschleunigt.

Ein Mikrocontroller (Atmel ATMEGA328p) steuert die Betriebsmodi des Speeders. Er überwacht den Datenbus der 6502-CPU des internen 1571-Diskettenlaufwerks und schaltet die entsprechenden ROM-Bänke automatisch um, sobald ein bestimmtes Kommando (Zeichenkette) erkannt wird. Der U32-Kernal-Adapter ist ebenfalls mit dem Speeder verbunden, sodass der Mikrocontroller die 8 ROM-Bänke synchron schalten kann. Dies bedeutet, dass der zum 1571-DOS-Kernal passende Kernal für den C128- oder C64-Modus automatisch aktiviert wird. Die 8 C128/C64-Kernals befinden sich ebenfalls in einem EPROM (27C040 oder 29F040).



## Teile

Der "Switchless 8x Multi-Floppy-Speeder" für den Commodore C128DCR besteht auf folgenden Teilen:

1. Multi-Speeder-Platine für Sockel der 1571 CPU 6502 AD (U101)

2. Parallelport-Adapter-Platine für CIA2 6526 (U4 C128) mit Parallelkabel (optional für DolphinDos3)

3. C128/C64 Kernal-Switcher-Platine für 27256 ROM1 (U32)
   
   

### (1) Multi-Speeder-Platine

<img title="8x Multi-Speeder 32KB RAM Expansion Module (DolphinDos 3)" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0a_Multi-Speeder.jpg" alt="loading-ag-1229" style="zoom:25%;" data-align="center">

Die Multi-Speeder-Platine wird anstelle der CPU 6502 AD des internen 1571 Diskettenlaufwerks eingesetzt. Die CPU wird dann auf den 6502 Sockel der Multi-Speeder-Platine gesetzt. In den meisten fällen ist die CPU auf dem C128DCR Motherboard aufgelötet, sodass diese erst ausgelötet und durch einen 40 Pin DIP Sockel ersetzt werden muss, bevor die Multi-Speeder-Platine eingesetzt werden kann. Die Multi-Speeder-Platine stellt das Herzstück dar, es stellt die gewählten DOS-Kernals der 1571, das zusätzliche RAM 32KB in 4x 8KB Bänke und den PIA 6821/6521 für den Parallelport und die Steuerung der RAM Bänke zur Verfügung. Die DOS-Kernals werden in einen 512KB EPROM in 8x64KB Bänke organisiert. Der ATMega Microcontroller aktiviert dann die gewünsche ROM-Bank und damit das DOS-Kernal. Wird durch DOS-Kommandos eine andere DOS-Bank aktiviert, dann führt der ATMega Microkontroller einen Reset des Diskettenlaufwerkes durch, damit das neue DOS-ROM korrekt gestartet wird. Mit (J4) verfügt der Multi-Speeder über die Möglichkeit den Multi-Speeder manuel auf Bank 0 (RSTROM/PIN3) zurück zu setzen oder die ROM-Bank +1 (SELROM/PIN1) zu aktivieren. Der Microcontroller reagiert, wenn eines der Pins auf (GND/PIN2) gesetzt werden. Das ist hilfreich, wenn das Laufwerk abgestürzt ist und nicht mehr über DOS-Kommandos vom Computer reagiert. Beipielsweise wenn ein fehlerhaftes experimentelles DOS-ROM im EPROM aktiviert wurde.   



### (2) Parallelport-Adapter-Platine

<img title="8x Multi-Speeder Parallelport Adapter C128DCR for U4" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0a_Parallelport-Adapter.jpg" alt="8x Multi-Speeder Parallelport Adapter C128D for U4CR" style="zoom:25%;" data-align="center">

Die Parallelport-Adapter-Platine wird anstelle des CIA2 6526 (U4) auf dem C128DCR Motherboard eingesetzt. Der CIA 6526 wird dann auf den 40 Pin DIP Sockel des Adapters gesetzt. Dieser Adapter ersetzt den Userport-Platinenstecker, der normalerweise verwendet wird. So bleibt jetzt der Userport des C182DCR nach außen frei und es braucht kein Parallel-Kabel nach außen geführt werden.  Zu der Parallelport-Adapter-Platine gehört auch ein 10 poliges Fachbandkabel das mit der Multi-Speeder-Platine verbunden werden muss. Dieses Adapter-Platine und das Flachbandkabel wird nur benötigt, wenn man das 1571 Diskettenlaufwerk im Parallelport-Modus mit DolphinDos3 betreiben möchte.



### (3) C128/C64 Kernal-Switcher-Platine

<img title="8x Multi-Floppy-Speeder Kernal Switcher C128DCR" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0_U32_Kernal-Switcher-Platine.jpg" alt="8x Multi-Floppy-Speeder Kernal Switcher C128DCR" style="zoom:25%;" data-align="center">

Die Kernal-Switcher-Platine ist eine Adapterplatine für ein 512KB EPROM 27C040 oder 29F040 für die 8x64KB Kernal ROM Bänke. Er wird im C128DCR in den Sockel U32 eingesetzt. Der Switcher verfügt über einen Anschluss A16/A17/A18 der mit der Multi-Speeder-Platine (J6) verbunden werden muss. Die Multi-Speeder-Platine schaltet dann neben dem Kernal des Diskettenlaufwerks auch die gleiche Bank des C128/C64 Kernal ROM um. Somit können 1571 Kernal und C128/C64 Kernal mit DOS-Kommandos parallel umgeschaltet werden. Es werden immer die gleichen ROM-Bänke aktiviert. Wenn DOS Kernal Bank 0 aktiv ist, dann ist auch das C128/C64 Kernal Bank 0 aktiv.



## ROM/RAM Organisation

Die Firmware (Kernals) für das 1571 Diskettenlaufwerk und C128/C64 werden jeweils in einem 512KB EPROM vom Typ 27C040 oder 29F040 (PLCC32) in jeweils 8x 64KB Bänke organisiert. Jede Bank 0-7 stellt den kompletten 64KB Adressenbereich dar.

Hier habe ich Test-Kernals zur Verfügung gestellt [[hier]](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/kernals).

### 512 KB ROM Internes 1571 Diskettenlaufwerk

Der Adressendekoder der Multi-Speeder-Platine blendet im Diskettenlaufwerk jeweils das ROM in den bereichen `$8000 bis $FFFF` ein.

### 32KB RAM Erweiterung des 1571 Diskettenlaufwerks

Das 1571 Diskettenlaufwerk hat wie das 1541 Diskettenlaufwerk standardmäßig nur 2KB Arbeitsspeicher. Das ist sehr eng bemessen und damit kann kein ganzer Track in den Arbeitsspeicher eingelesen werden. DolphinDOS 3 nutzt deshalb zusätzlichen Speicher und liest bei einer Diskettendrehung einen kompletten Track von der Diskette ein. Dazu wird mindestens 8KB zusätzlicher RAM-Speicher benötigt. Der Multi-Speeder verfügt über ein 62256 32KB SRAM oder 6264 8KB SRAM. Dieser zusätzliche 8KB Speicherbereich wird im CPU-Adressenraum bei `6000 - 7FFF` im Speicher des 1571 Diskettenlaufwerks zur Verfügung gestellt. Bei der Nutzung eines 32KB SRAM können die 8K Bänke des Speicher über den PIA Baustein Port PB0 und PB1 geschaltet werden. Bei Nutzung des 32KB SRAM müssen Jumper A14RAM (J7) und A15RAM (J8) auf dem Multi-Speeder-Platine geschlossen werden, damit das Bankswitching funktioniert.



### Memory Map 1571 Diskettenlaufwerk

| Adresse         | Bereich                        |
| --------------- | ------------------------------ |
| `$0000 - $07FF` | 2KB RAM (Standard)             |
| `$1800 - $180f` | VIA 1 6522 (IEC Bus und Drive) |
| `$1C00 - $1C0f` | VIA 2 6522 (Signal, Motor)     |
| `$2000 - $4000` | Gate Array (CIA/WD MFM)        |
| `$5000 - $5FFF` | PIA 6821/6521 *2)*             |
| `$6000 - $7FFF` | SRAM 8KB/ 32KB Bank 0-3 *2)*   |
| `$8000 - $FFFF` | 1571 DOS Kernal Bank 0-7 *2)*  |

*2)* Zusätzlich durch den Multi-Floppy-Speeder bereitgestellt



## Switchless - Wahl der Betriebsmodi (ROM-Bank)

### Wechseln der ROM-Bank

Die Bank 0 - 7 werden mit den Befehlen 1@RNROM bis 8@RNROM aufgerufen.

Der Wechsel der Speeder kann am Computer durch einfache Befehle ausgelöst werden. Dieses Beispiel zeigt den Wechsel im C64 Modus:

1. **Wechsel zu Bank 2 JiffyDos 64):**
   
   ```plaintext
   LOAD"3@RNROM",8,1
   ```
   
   Das Laufwerk wechselt zu Bank 2 und startet automatisch neu.

2. **Wechsel zu Bank 0 (DolphinDos 3):**
   
   ```plaintext
   OPEN 1,8,15,"I:1@RNROM":CLOSE 1
   ```
   
   Der Mikrocontroller wechselt zu Bank 0, die Laufwerks LED blinkt, und das Laufwerk startet neu.

3. **Wechsel zu Bank 7 (CBMDOS):**
   
   ```plaintext
   @I:8@RNROM
   ```
   
   Der Mikrocontroller erkennt den Befehl und wechselt zu Bank 7. Die LED blinkt und das Laufwerk startet neu.

4. **Temporäre Deaktivierung des Switchless-Modus:**
   
   ```plaintext
   @I:0@RNROM oder LOAD"0@RNROM",8,1
   ```
   
   Der Switchless-Modus wird vorübergehend deaktiviert, bis das Laufwerk neu gestartet wird.
   
   

**Hinweis:**

Wenn das Diskettenlaufwerk 1571 im 2-MHz-Modus läuft (C128-Modus/DolphinDos), kann es vorkommen, dass die ROM-Umschaltung nicht immer zuverlässig funktioniert. Der Mikrocontroller ATmega328 hat dann Timingprobleme beim Lesen der Befehle vom Datenbus. Zuverlässig funktioniert es, wenn man den Quarz Y1 auf der Platine von 20 MHz auf 22,1184 MHz wechselt. Zwar gibt der Hersteller die maximale Taktrate für den ATmega328 mit 20 MHz an, aber in der Praxis läuft der Mikrocontroller auch problemlos mit 22 MHz.



## Übersicht der C128/C64 und DOS-Kernals

### C128/C64 Kernals U32

Die C128/C64 Kernal-Switcher-Platine für den U32 Sockel ist wie folgt organisiert. Wichtig ist zu beachten, dass derzeit bei dem 512KB EPROM 27C040 und 29F040 immer nur der obere ROM-Bereich 32KB der 64KB Bänke von `$x8000 - $xFFFF` genutzt wird. Somit müssen die Kernals ab `$x8000` platziert werden



Das Kernal ROM 27256 (U32) (C128/C64 Kernals) ist beim C128DCR grundsätzlich wie folgt aufgebaut:

| ROM Adressenbereich | ROM Typ                      |       |
| ------------------- | ---------------------------- | ----- |
| `$0000 - $1FFF`     | C64 Basic V2 `$A000 - $BFFF` | 8KB   |
| `$2000 - $3FFF`     | C64 Kernal  `$E000 - $FFFF`  | 8KB   |
| `$4000 - $7FFF`     | C128 Kernal/System           | 16 KB |



### 1571 DOS Kernal (U101 Multi-Speeder)

Das Kernal ROM des Laufwerks beginnt bei `$x8000 - $xFFFF` und je nach aktiver Bank 0-7 wird der entsprechende Bereich dort in den Adressenraum der CPU eingeblendet.



| Bank | Switch  | Eprom Adresse     | CPU             |
| ---- | ------- | ----------------- | --------------- |
| 0    | 1@RNROM | `$08000 - $0FFFF` | `$8000 - $FFFF` |
| 1    | 2@RNROM | `$18000 - $1FFFF` | `$8000 - $FFFF` |
| 2    | 3@RNROM | `$28000 - $2FFFF` | `$8000 - $FFFF` |
| 3    | 4@RNROM | `$38000 - $3FFFF` | `$8000 - $FFFF` |
| 4    | 5@RNROM | `$48000 - $4FFFF` | `$8000 - $FFFF` |
| 5    | 6@RNROM | `$58000 - $5FFFF` | `$8000 - $FFFF` |
| 6    | 7@RNROM | `$68000 - $6FFFF` | `$8000 - $FFFF` |
| 7    | 8@RNROM | `$78000 - $7FFFF` | `$8000 - $FFFF` |



ROM Bank-Belegung anhand meiner Beispielkonfiguration:

| Bank | Switch  | System            | U32 C128 | U32 C64      | U101 1571    | EPROM           |
| ---- | ------- | ----------------- | -------- | ------------ | ------------ | --------------- |
| 0    | 1@RNROM | CBM               | CBM      | CBM          | CBM          | `$08000-$0FFFF` |
| 1    | 2@RNROM | CBM RAM Exp       | CBM      | CBM          | CBM RAM Exp. | `$18000-$1FFFF` |
| 2    | 3@RNROM | DolphinDos 3      | DD3      | DD3          | DD3          | `$28000-$2FFFF` |
| 3    | 4@RNROM | DolphinDos 3      | DD3      | DD3-Custom   | DD3          | `$38000-$3FFFF` |
| 4    | 5@RNROM | CBM-DD-SD2IEC     | CBM      | DD-JD-SD2IEC | CBM RAM Exp. | `$48000-$4FFFF` |
| 5    | 6@RNROM | CBM               | CBM      | JaffyDos 1.3 | CBM RAM Exp. | `$58000-$5FFFF` |
| 6    | 7@RNROM | CBM (reserved JD) | CBM      | CBM          | CBM RAM Exp. | `$68000-$6FFFF` |
| 7    | 8@RNROM | CBM (reserved JD) | CBM      | CBM          | CBM RAM Exp. | `$78000-$7FFFF` |

"CBM RAM Exp." ist das original CBMDOS der 1571 mit einem Patch für die RAM-Erweiterung des Multi-Speeders. Dieser Patch enthält einen TrackCache und so kann das 1571 Diskettenlaufwerk einen kompletten Track auf einmal einlesen. Das JiffyDOS 128 gibt es auch in einer Version mit dem Patch und beschleunigt das lesen nochmal um 20%.



Weitere Informationen dazu auf Github von ytmytm: [GitHub - ytmytm/1571-TrackCacheROM: A firmware patch for Commodore 1571 drive and internal C128D drive enabling RAM expansion use for track cache](https://github.com/ytmytm/1571-TrackCacheROM) 



JiffyDOS 128 läuft perfekt auf dem Multi-Speeder. Besonders mit dem RAM-Expansion Patch ist JiffyDOS im C128 und C64 nochmal erheblich schneller. JiffyDOS habe ich nicht zum Download angeboten, da es noch kommerziell vertrieben wird.



**Bitte beachten das beim Betrieb der Multi-Speeder-Platine das original DOS-ROM U102 ersatzlos herausgenommen werden muss, da der Multi-Speeder jetzt über das eigene EPROM das gewählte DOS-Kernal zur Verfügung stellt! Der Verbleib würde ein Adressenkonflikt erzeugen und das Diskettenlaufwerk würde nicht mehr korrekt funktionieren**



**Beim umschalten kann es Probleme geben, wenn das Diskettenlaufwerk im 2MHz modus betrieben wird. Dann einfach mehrmals z.B. mit (LOAD"x@RNROM",8,1) das gewünschte ROM versuchen umschalten. Das Problem liegt am Timing in Verbindung mit dem ATMega und 74AHTC273 Flip-Flop unter 2MHz. Am besten funktioniert das System mit einem 74AHTC273 von NXP. Diese sind aber schwer verfügbar.** 



## Periphal interface Adapter (PIA)

Der Periphal interface Adapter (PIA) steuert die parallele Datenübertragung des Diskettenlaufwerks mit dem C128/C64 über die Parallelport-Adapter-Platine oder einem Parallel Userport Kabel. Getestet habe ich folgende PIA Versionen:

1. MC6821P (Motorola)

2. W65C21S6TPG-14 (Western Design Center)

3. EF68B21 (STMicroelectronics) 
   
   

## Bill of Materials

### BOM - Multi-Speeder

| Reference                           | Value                            | Datasheet                                                                                                                                                            | Footprint                                                                                           | Qty | DNP | Note                                                                                                                                                                                          |
| ----------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --- | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PCB 8xMulti-Speeder-PCB for C128DCR |                                  |                                                                                                                                                                      |                                                                                                     | 1   |     |                                                                                                                                                                                               |
| C1,C2,C5,C6,C7                      | Capacitor 0,1uF                  | https://www.aliexpress.com/item/1005002771940165.html                                                                                                                | C_Disc_D3.0mm_W2.0mm_P2.50mm                                                                        | 5   |     |                                                                                                                                                                                               |
| C3,C4                               | Capacitor 22 pF                  | https://www.aliexpress.com/item/1005002771940165.html                                                                                                                | C_Disc_D3.0mm_W2.0mm_P2.50mm                                                                        | 2   |     |                                                                                                                                                                                               |
| CN1                                 | Connector                        | https://www.aliexpress.com/item/1005008071308576.html                                                                                                                | MicroMatch 1,27 mm,2X05 (MICMA10B)                                                                  | 1   |     | recommend                                                                                                                                                                                     |
| D1                                  | LED GREEN                        |                                                                                                                                                                      | LED_THT:LED_D3.0mm                                                                                  | 1   |     |                                                                                                                                                                                               |
| R2,R4,R5                            | Resistor 10K,1/4W                |                                                                                                                                                                      | R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal                                                    | 3   |     |                                                                                                                                                                                               |
| R3                                  | Resistor 560R, 1/4               |                                                                                                                                                                      | R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal                                                    | 1   |     |                                                                                                                                                                                               |
| SW1                                 | JTP-1130                         | https://www.aliexpress.com/item/1005005810426286.html                                                                                                                | 6X6x5mm 4PIN dip TACT push button switch Micro key power tactile switches 6x6x5 6*6*5MM Light touch | 1   |     |                                                                                                                                                                                               |
| U1                                  | Socket                           |                                                                                                                                                                      | DIP-40_W15.24mm_Socket                                                                              | 2   |     |                                                                                                                                                                                               |
| U2                                  | Pin Header                       | https://www.aliexpress.com/item/1005007564228387.html                                                                                                                | 2.54mm Pin Header Male Single Row 20/40 Pin 2.54mm Round Pin Connector                              | 2   |     |                                                                                                                                                                                               |
| U3                                  | Socket                           |                                                                                                                                                                      | PLCC-32_THT-Socket                                                                                  | 1   |     |                                                                                                                                                                                               |
| U3                                  | EPROM 29F040                     | https://www.aliexpress.com/item/1005007299303666.html                                                                                                                | PLCC-32                                                                                             | 1   |     | alternativ 27C040 PLCC-32                                                                                                                                                                     |
| U4                                  | IC W65C21S6TPG-14                | https://www.mouser.de/datasheet/2/436/w65c21-661.pdf <br/>https://de.aliexpress.com/item/1005006827509758.html<br/>https://de.aliexpress.com/item/4001175531491.html | DIP-40 W15.24mm                                                                                     | 1   |     | alternativ<br/>MC68B21P, R65C21P2                                                                                                                                                             |
| U5                                  | IC 74AHCT273D                    | https://www.nexperia.com/product/74AHCT273D                                                                                                                          | DIP-28_W7.62mm                                                                                      | 1   |     | Am besten funktionieren die 74AHCT273D von Nexperia. Bei anderen Herstellern kann es sonst im 2MHz zu Problemen bei der ROM Umschaltung kommen.                                               |
| U6                                  | IC ATmega328P                    | https://www.aliexpress.com/item/32901846548.html                                                                                                                     | Package_DIP:DIP-28_W7.62mm                                                                          | 1   |     |                                                                                                                                                                                               |
| U7                                  | IC ATF16V8B                      | https://www.aliexpress.com/item/4000830127120.html                                                                                                                   | Package_DIP:DIP-20_W7.62mm                                                                          | 1   |     | GAL16V8                                                                                                                                                                                       |
| U8                                  | IC HM62256LFP-12T SRAM 32KB      | https://www.aliexpress.com/item/1005006266772362.html                                                                                                                | Package_SO:SOP-28_8.4x18.16mm_P1.27mm                                                               | 1   |     | alternativ<br/>LY62256SL-70LL<br/>UT62256CSC-70LL<br/>CY62256NL-70SNXC                                                                                                                        |
| Y1                                  | Crystal 22.1184 MHz HC-49S       | https://www.aliexpress.com/item/1005007425032260.html                                                                                    | Crystal_HC49-4H_Vertical                                                                            | 1   |     | Hersteller gibt 20MHz als maximalen Takt für den ATMega 328 an. Jedoch kann das zu Timingproblemen beim ROM-Umschaltung im 2MHz Modus der 1571 führen. Ein 22.1184 MHz Takt löst das Problem. |
| PCB                                 | PCB 8x Multi-Speeder for C128DCR |                                                                                                                                                                      |                                                                                                     | 1   |     |                                                                                                                                                                                               |
| CN2                                 | Connector                        | https://www.aliexpress.com/item/1005004266492521.html                                                                                                                | IDC-Header_2x05_P2.54mm_Vertical                                                                    | 1   |     | optional                                                                                                                                                                                      |
| R1                                  | Resistor 3,3K, 1/4W              |                                                                                                                                                                      | R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal                                                    | 1   |     | optional only for W65C02 WDC CPU                                                                                                                                                              |
| J4                                  | Connector                        | https://www.aliexpress.com/item/4000694229610.html                                                                                                                   | PinHeader_1x03_P2.54mm_Vertical                                                                     | 1   |     | optional                                                                                                                                                                                      |
| J5                                  | Connector                        | https://www.aliexpress.com/item/4000988113226.html                                                                                                                   | PinHeader_2x03_P2.54mm_Vertical                                                                     | 1   |     | optional                                                                                                                                                                                      |
| J6                                  | Connector                        | https://www.aliexpress.com/item/4000694229610.html                                                                                                                   | PinHeader_1x03_P2.54mm_Vertical                                                                     | 1   |     | optional                                                                                                                                                                                      |



### BOM - Parallelport-Adapter-Platine

| Reference                        | Value                                                  | Datasheet                                             | Footprint                                                                                                                | Qty | DNP | Note      |
| -------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --- | --- | --------- |
| PCB Parallelport-Adapter-Platine |                                                        |                                                       |                                                                                                                          | 1   |     |           |
| CN1                              | Connector                                              | https://www.aliexpress.com/item/1005008071308576.html | MicroMatch 1,27 mm,2X05 (MICMA10B)                                                                                       | 1   |     | recommend |
| U4                               | Gold Round Female Male Pin Sensor Crystal Socket       | https://www.aliexpress.com/item/32972142300.html      | D0.5mm D0.45-0.6mm PCB Gold Round Female Male Pin Sensor Crystal Socket Dim1.4*7.4mm,No Plastic for 2.54 Hole Pin Header | 40  |     |           |
| CN2                              | Connector                                              | https://www.aliexpress.com/item/1005004266492521.html | IDC-Header_2x05_P2.54mm_Vertical                                                                                         | 1   |     | optional  |
| Cable                            | Flat Ribbon                                            | https://www.aliexpress.com/item/1005004316520454.html | 1.27mm PITCH color Flat Ribbon Cable Rainbow DuPont Wire for FC dupont Connector 2.54mm IDC                              | 1   |     |           |
| CN1                              | Micromatch IDC Header Connector                        | https://www.aliexpress.com/item/4001278233965.html    | Micromatch Red 2.54mm Pitch Double Row Female IDC Box Header Connector 10P 2x05                                          | 2   |     |           |
| CN2                              | tch Female IDC Socket Connector Ribbon Cable Connector | https://www.aliexpress.com/item/1005002804645942.html | 2.54mm Pitch Female IDC Socket Connector Ribbon Cable Connector 10 PIN                                                   | 2   |     | optional  |



### BOM - C128/C64 Kernal-Switcher-Platine

| Reference                            | Value        | Datasheet                                             | Footprint                                                           | Qty | DNP | Note                      |
| ------------------------------------ | ------------ | ----------------------------------------------------- | ------------------------------------------------------------------- | --- | --- | ------------------------- |
| PCB C128/C64 Kernal-Switcher-Platine |              |                                                       |                                                                     | 1   |     |                           |
| J3                                   | Connector    | https://www.aliexpress.com/item/4000694229610.html    | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical          | 1   |     |                           |
| U1                                   | Pin Header   | https://www.aliexpress.com/item/1005007564228387.html | 2.54mm Pin Header Male Single Row 14 Pin 2.54mm Round Pin Connector | 2   |     |                           |
| U2                                   | Socket       |                                                       | PLCC-32_THT-Socket                                                  | 1   |     |                           |
| U2                                   | EPROM 29F040 | https://www.aliexpress.com/item/1005007299303666.html | PLCC-32                                                             | 1   |     | alternativ 27C040 PLCC-32 |



## ATMega 328P

Der Atmel ATMega 328P Microcontroller überwacht den Datenbus und steuert die ROM-Bänke und ist für den Wechsel der Betriebsmodi zuständig. Die Firmware kann über ein Arduino Board oder einen AV Programmer programmiert werden. Ich nutze den XGecu T48 Universal Programmer über eine .mpj Projektdatei. Beim programmieren mit dem XGecu mit der .mpj Datei bitte das EEPROM nicht mit programmieren, da es sonst eine Fehlermeldung gibt. Dieses kann man im Menü des XGecu deaktivieren.



<img title="" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/XGecuT48UniversalProgrammerEEPROM.png" alt="" data-align="center" style="zoom:25%;">

<img title="" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/XGecuT48UniversalProgrammerConfig.png" alt="" style="zoom:25%;" data-align="center">

## Installation C128DCR

<img title="8x Multi-Speeder Install C128DCR  Mainboard" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0_C128DCR_Overview.jpg" alt="8x Multi-Speeder Install C128DCR  Mainboard" style="zoom:50%;" data-align="center">

Die Installation des Multi-Speeders auf dem C128DCR Mainboard. Der Multi-Speeder wird anstelle der 6502 CPU (U101) eingesetzt. Die 6502 CPU wird auf den CPU-Sockel des Multi-Speeder gesetzt (unten rechts). Der Kernal-Switcher befindet sich unten links und wird anstelle des original Kernals auf den Sockel (U32) gesetzt. Der Parallel-Adapter kommt anstelle des CIA 6526 (U4) in einen Sockel. Der CIA 6526 wird auf den Parallel-Adapter-Platine gesetzt. Der Kernel-Switcher wird mit einem drei PIN Kabel mit dem Multi-Speeder verbunden. Der Parallel-Adapter wird mit einen 10 poligen Kabel ebenfalls mit der Multi-Speeder-Platine verbunden (Parallelport).

## Downloads

1. [ATF16V8 (GAL16V8) Dateien](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/pld-atf16v8-gal16v8)

2. [ATMEL ATMega328 P Dateien](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/atmega328p)

3. [Gerber-Dateien zur Platinenherstellung](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/gerber)

4. [Schaltpläne zum 8x Multi-Speeder 32KB RAM Expansion (DolphinDos3)](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/schematics)

5. [Fotogalerie](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/images)

6. [Weitere Dokumente](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/docs)
   
   

## Shared Projects auf PCBWay.com

1. [8x Multi-Floppy Speeder 32KB RAM Expansion für den Commodore C128DCR](https://www.pcbway.com/project/shareproject/Switchless_8x_Multi_Floppy_Speeder_with_32_KB_RAM_Expansion_for_the_Commodore_C1_557a83c8.html)

2. [C128/C64 Kernal-Switcher für 8x Multi-Floppy-Speeder C128DCR](https://www.pcbway.com/project/shareproject/C128_C64_U32_Kernal_Switcher_Adapter_for_Switchless_8x_Multi_Floppy_Speeder_with_f113e895.html)

3. [Parallel-Port-Adapter für 8x Multi-Floppy-Speeder C128DCR](https://www.pcbway.com/project/shareproject/Parallelport_Adapter_U4_for_Switchless_8x_Multi_Floppy_Speeder_with_32_KB_RAM_Ex_558623e7.html)
   
   

## Hilfreiche Links

1. DolphinDos [Dolphin DOS – C64-Wiki](https://www.c64-wiki.de/wiki/Dolphin_DOS) & https://project64.c64.org/hw/dolphindos.txt

2. RAMBoard: [RAMBOard – C64-Wiki](https://www.c64-wiki.de/wiki/RAMBOard) & [https://www.c64copyprotection.com/ramboard/](https://www.c64copyprotection.com/ramboard/) & [[CSDb] - Super-Card 6 Plus RAMboard [scpu] by Master (2018)
   
   

## Danke

Zu diesem Projekt haben viele beigetragen und ist das Ergebnis vieler Entwickler. Besonders möchte ich mich bei folgenden Entwicker bedanken.

1. Jan Bubela und Gunther Jilg die DolphinDos entwickelt haben.

2. RetroNynjah hat mir geholfen seinen Switchless Multi-ROM auf den 8x Multi-Speeder zu integrieren. [GitHub - RetroNynjah/Switchless-Multi-ROM-for-27128-27256](https://github.com/RetroNynjah/Switchless-Multi-ROM-for-27128-27256)

3. Die hilfreiche Seite mit technischen Daten zu DD3 von silverdr. [https://e4aws.silverdr.com/projects/dolphindos3/](https://e4aws.silverdr.com/projects/dolphindos3/)

4. Ytmytm für seinen TrackCache: [GitHub - ytmytm/1571-TrackCacheROM: A firmware patch for Commodore 1571 drive and internal C128D drive enabling RAM expansion use for track cache](https://github.com/ytmytm/1571-TrackCacheROM) 
   
   

## Haftungsausschluß

Ich habe dieses Projekt mit großer Sorgfalt gestaltet und getestet. Aber Fehler können immer passieren. Dieses Projekt ist ein Hobbyprojekt. Ich übernehme deshalb keine Garantie für die Funktion oder für etwaige Schäden, die durch den Einbau oder die Nutzung dieses Projektes in jeglicher Art entstehen könnten.



## Spenden

Ich habe viele Stunden an diesem Projekt gearbeitet. Wenn Du diese Arbeit unterstützen möchtest, dann kannst Du mir etwas für die Kaffekasse spenden. Vielen Dank! [Paypal Spende hier klicken!](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=Q8HXKYARXKT4L&ssrt=1714757590172)



## Nutzungsrecht / Copyright

Du kannst diese Projekt gerne für private zwecke nutzen. Die kommerzielle Nutzung wie z.B. Verkauf oder andere Verbreitung meines Multi-Floppy-Speeders ist ohne meine Erlaubnis untersagt.



Ich wünsche euch viel Freude mit meinem 8x Multi-Floppy-Speeder 32KB RAM Expansion für den C128D CR.



Viele Grüße
Frank Eggen 



## Update

- 2024-12-07 PCB-Gerberdatei Update auf Version 2.0b - Fehler R2 und R3 bereinigt. Zwischen Pull-Up-Widerständen R2-R3 müssen 5V anliegen.
