# Switchless 8x Multi-Floppy-Speeder V3.3 mit 512 KB RAM-Erweiterung für den Commodore C128 DCR und das interne 1571-Diskettenlaufwerk (DolphinDOS 3 / neues DolphinDos 25)

<img title="8x Multi-Floppy-Speeder 32KB RAM Expasion for the internal 1571 Floppydrive C128DCR - DolphinDos 3" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0_C128DCR_Multi-Floppy-Speeder-Set-Title.jpg" alt="loading-ag-1227" data-align="center" style="zoom:25%;">

## Beschreibung

Dieses Projekt ist eine Weiterentwicklung des sehr schnellen und beliebten DolphinDos 3 für den C128 und das 1571-Diskettenlaufwerk. Es kombiniert das Beste aus der Retro-Welt mit moderner Technik und war in dieser Form bisher nicht verfügbar. Der **switchless 8x Multi-Floppy-Speeder** läuft nicht nur mit DolphinDos 3, sondern ermöglicht den Betrieb von bis zu acht DOS-Kernals sowie C128- und C64-Kernals, die komfortabel per DOS-Kommandos aktiviert werden können. Dadurch kann neben dem originalen CBM-DOS und DolphinDos 3 beispielsweise auch JiffyDOS 128 genutzt werden. Zudem ist bei JiffyDOS eine Version mit einem **TrackCache** verfügbar, die JiffyDOS noch einmal erheblich beschleunigt.  Das sorgt für maximale Kompatibilität.  

Die Version **3.x** verfügt jetzt über **512 KB RAM**, im Gegensatz zur Version **2.x** mit nur **32 KB RAM**. In Kombination mit dem **Peripheral Interface Adapter (PIA, Typ 6821 oder 6521)** ermöglicht sie eine ultraschnelle parallele Datenübertragung sowie die Steuerung der **64 x 8 KB RAM-Bänke (512 KB)**.  

Mit dem erweiterten **DolphinDos 25** kann das Diskettenlaufwerk selbstständig über DOS-Befehle eine komplette Diskette in den **erweiterten 512 KB Speicher** in zwei RAM-Seiten einlesen und anschließend auf eine neu formatierte Diskette zurückschreiben. Dies geschieht besonders schnell, da keine Datenübertragung zum Computer erforderlich ist.  

Alle Komponenten des Multi-Speeders für den **C128DCR** sind intern verbaut. Der interne **Kernal-Switcher** schaltet synchron das passende C128-/C64-Kernal um, während die interne **Parallelport-Adapter-Platine** für eine parallele Datenübertragung sorgt. Der **Userport** bleibt von außen ungenutzt.  

Der **switchless 8x Multi-Floppy-Speeder** mit **512 KB RAM-Erweiterung** für den **Commodore C128DCR** ist einer der universellsten Beschleuniger für das interne **1571-Diskettenlaufwerk** des C128DCR.  

Zusätzlich ist der **switchless 8x Multi-Floppy-Speeder** vollständig **RAMBoard-kompatibel**, was den Einsatz entsprechender **Nibble-Kopierprogramme**, die RAMBoard unterstützen, ermöglicht.  



Diesen Multi-Speeder habe ich ebenfalls für die **externen Diskettenlaufwerke 1571, 1541 und 1541-II** mit verschiedenen passenden **PCBs** entwickelt. Diese können miteinander kombiniert betrieben werden.  

---

## Funktionen

1. 8 x 64 KB Kernals-ROM-Bänke für C128/C64-Modus
2. 8 x 64 KB DOS-ROM-Bänke für das interne 1571-Diskettenlaufwerk
3. C64/C128 und DOS-Kernal lassen sich (switchless) per DOS-Kommandos umschalten.
4. 512 KB RAM-Erweiterung für das 1571-Diskettenlaufwerk (64 Bänke, schaltbar über PIA)
5. Parallelport für das 1571-Diskettenlaufwerk (PIA 6821/W65C21)
6. U32-Kernal-Adapter-Sockel für die C128/C64 8x-Kernal-Umschaltung (Switchless)
7. U4 6526-CIA-Adapter für den Parallelport des internen 1571-Diskettenlaufwerks
8. Neue nützliche Fuktionen mit DolphinDos 25 
9. Kompatibilität mit RAMBoard für Nibbler-Kopierprogramme

---

## Funktionsweise

In einem **512 KB EPROM** (Typ **27C040** oder **29F040**, U3) können bis zu acht **Kernal-Betriebssysteme** für das **1571-Diskettenlaufwerk** gespeichert werden. Ein **Peripheral Interface Adapter (PIA)** vom Typ **6821** oder **W65C21** (U4) erweitert das Diskettenlaufwerk um einen zusätzlichen **8-Bit-Parallelport**.  

Zusammen mit der **512 KB RAM-Erweiterung (U8)** ist es möglich, **DolphinDos 3** und mein neues, angepasstes **DolphinDos 25** zu betreiben. Dadurch kann das Laufwerk komplette **Tracks in einem Durchgang einlesen**, was beispielsweise das **Laden von Programmen mit DolphinDos im C128- und C64-Betrieb um den Faktor 38** beschleunigt. Mit **DolphinDos 25** (derzeit in Entwicklung) können ganze Disketten in den **512 KB RAM geladen und anschließend zurück auf Disketten geschrieben** werden.  

Ein **Mikrocontroller (Atmel ATMEGA328p)** steuert die **Betriebsmodi des Speeders**. Er überwacht den **Datenbus der 6502-CPU** des Diskettenlaufwerks und schaltet die entsprechenden **ROM-Bänke** automatisch um, sobald ein bestimmtes Kommando (Zeichenkette) erkannt wird.  

Der **U32-Kernal-Adapter** für den **C128-/C64-Modus** ist ebenfalls mit dem Speeder verbunden, sodass der Mikrocontroller die **acht ROM-Bänke synchron** schalten kann. Dies bedeutet, dass der zum **1571-DOS-Kernal passende Kernal für den C128- oder C64-Modus** automatisch aktiviert wird. Die **acht C128-/C64-Kernals** befinden sich ebenfalls in einem **EPROM** vom Typ **27C040** bzw. **29F040**.  

---

### 512 KB ROM- und RAM-Erweiterung für das 1571-Diskettenlaufwerk

Das **32 KB ROM** mit der **Firmware für das 1571-Diskettenlaufwerk** befindet sich normalerweise im **Adressbereich** `$8000 - $FFFF`. Der **Multi-Speeder** stellt zusätzliche **ROM-Bereiche für weitere DOS-Routinen** im Bereich `$3000 - $3FFF` zur Verfügung. Dadurch können im **27C040- oder 29F040-EPROM** des Multi-Speeders (U3) in den Bereichen `$x3000 - $x3FFF` und `$x8000 - $FFFF` **eigene, beliebige Firmware** bereitgestellt werden.  

Das **1571-Diskettenlaufwerk** verfügt – ebenso wie das **1541-Diskettenlaufwerk** – standardmäßig nur über **2 KB Arbeitsspeicher**. Das ist äußerst knapp bemessen, wodurch das Laufwerk beim **Einlesen eines Tracks** stark eingeschränkt ist. **DolphinDos 3** nutzt daher **8 KB zusätzlichen Speicher**, sodass bei einer **einzigen Diskettenumdrehung** ein kompletter Track in den Arbeitsspeicher eingelesen und geschrieben werden kann. Dies beschleunigt die **Lesegeschwindigkeit erheblich**. Normalerweise steht dem Diskettenlaufwerk lediglich ein **256-Byte-Puffer** zur Verfügung.  

Der **Multi-Speeder** verfügt über ein **AS6C4008 512 KB SRAM**. Dieses zusätzliche RAM wird in **64 Bänke** im **CPU-Adressraum** bei `$6000 - $7FFF` im Speicher des **1571-Diskettenlaufwerks** eingebunden. Bei der Nutzung eines **512 KB SRAM** können die **8 KB Speicherbänke** über den **PIA-Baustein** im Adressbereich `$5002 - $5003` über **Port PB0 bis PB5** umgeschaltet werden. Die **Bank 0** ist standardmäßig aktiviert.  

Am Ende der Dokumentation gibt es ein kleines **Assemblerprogramm**, das zeigt, wie das **Bank-Switching** funktioniert.  

---

### Memory Map 1571 Diskettenlaufwerk + C128DCR 1571 Multi-Speeder V3.3

| Adresse         | Bereich                                                     |
| --------------- | ----------------------------------------------------------- |
| `$0000 - $07FF` | 2KB RAM (Standard)                                          |
| `$1800 - $180f` | VIA 1 6522 (Serieller Bus)                                  |
| `$1C00 - $1C0f` | VIA 2 6522 (Laufwerkssteuerung)                             |
| `$2000 - $2FFF` | (Gatearry / WD 1770 / MFM)                                  |
| `$3000 - $3FFF` | exp. DOS-ROM (z.B. DolphinDos 25 Routinen) [^1]             |
| `$4000 - $4FFF` | CIA 6526                                                    |
| `$5000 - $5FFF` | PIA 6821/W65C21 [^1]                                        |
| `$6000 - $7FFF` | SRAM 8KB / 512KB Bank 0 - 63 (64 Bänke) default Bank 0 [^1] |
| `$8000 - $FFFF` | 1571 DOS Kernal Bank [^1]                                   |

 [^1] Zusätzlich durch den Multi-Floppy-Speeder bereitgestellt.

---

## Teile

Der "Switchless 8x Multi-Floppy-Speeder" für den Commodore C128DCR besteht auf folgenden Teilen:

1. Multi-Speeder-Platine für Sockel der 1571 CPU 6502 AD (U101)

2. Parallelport-Adapter-Platine für CIA2 6526 (U4 C128) mit Parallelkabel (optional für DolphinDos3/DolphinDos25)

3. C128/C64 Kernal-Switcher-Platine für 27256 ROM1 (U32)

---   

### (1) Multi-Speeder-Platine

<img title="8x Multi-Speeder 32KB RAM Expansion Module (DolphinDos 3)" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/v3.3_C128DCR_1571_CPU_THT_DD3_Speeder (512KB)_pcb_real.jpg" alt="loading-ag-1229" style="zoom:25%;" data-align="center">

Die **Multi-Speeder-Platine** wird anstelle der **6502 AD-CPU (U101)** des internen **1571-Diskettenlaufwerks** auf das **Motherboard** eingesetzt. Die CPU wird dann auf den **6502-Sockel (U1)** der Multi-Speeder-Platine platziert. In den meisten Fällen ist die CPU jedoch direkt auf dem **C128DCR-Motherboard** aufgelötet. Daher muss sie zunächst ausgelötet und durch einen **40-Pin-DIP-Sockel** ersetzt werden, bevor die Multi-Speeder-Platine eingesetzt werden kann.  

Die **Multi-Speeder-Platine** bildet das **Herzstück** des Systems. Sie stellt die **gewählten DOS-Kernals für das 1571**, das **zusätzliche 512 KB RAM** (organisiert in **64 x 8 KB Bänke**) sowie den **PIA 6821/6521 I/O-Baustein für den Parallelport** bereit. Die **DOS-Kernals** werden in einem **512 KB EPROM** gespeichert und in **8 x 64 KB Bänke** organisiert. Der **ATMega-Mikrocontroller** aktiviert die gewünschte **ROM-Bank**, wodurch das entsprechende **DOS-Kernal** sowie das passende **C128-/C64-Kernal** über den **Kernal-Switcher** aktiviert wird.  

Wird per **DOS-Kommando** eine andere **DOS-Bank** aktiviert, führt der **ATMega-Mikrocontroller** einen **Reset des Diskettenlaufwerks** durch, sodass das neue **DOS-ROM mit der Firmware** korrekt gestartet wird.  

Die Multi-Speeder-Platine verfügt über **(J3)** eine Möglichkeit, den Multi-Speeder **manuell auf Bank 0** zurückzusetzen (**RSTROM/PIN 3**) oder die **ROM-Bank um +1** weiterzuschalten (**SELROM/PIN 1**). Der **Mikrocontroller** reagiert, wenn einer der **Pins mit (GND/PIN 2)** verbunden wird.  

Diese Funktion ist besonders hilfreich, wenn das **Laufwerk abgestürzt** ist und nicht mehr über **DOS-Kommandos** vom Computer aus reagiert – beispielsweise, wenn ein fehlerhaftes oder experimentelles **DOS-ROM im EPROM** aktiviert wurde.  

---

### (2) Parallelport-Adapter-Platine

<img title="8x Multi-Speeder Parallelport Adapter C128DCR for U4" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0a_Parallelport-Adapter.jpg" alt="8x Multi-Speeder Parallelport Adapter C128D for U4CR" style="zoom:25%;" data-align="center">

Die **Parallelport-Adapter-Platine** wird anstelle des **CIA2 6526 (U4)** auf dem **C128DCR-Motherboard** eingesetzt. Der **CIA 6526** wird dann in den **40-Pin-DIP-Sockel** des Adapters eingesetzt.  

Dieser Adapter ersetzt den **Userport-Platinenstecker**, der normalerweise verwendet wird. Dadurch bleibt der **Userport des C128DCR** von außen frei, und es ist kein externes **Parallelkabel** erforderlich.  

Zur **Parallelport-Adapter-Platine** gehört außerdem ein **10-poliges Flachbandkabel**, das mit der **Multi-Speeder-Platine** verbunden werden muss. Diese **Adapter-Platine** sowie das **Flachbandkabel** werden jedoch nur benötigt, wenn das **1571-Diskettenlaufwerk im Parallelport-Modus mit DolphinDos 3** betrieben werden soll.  

In der neuesten Version verfügt die **Parallelport-Adapter-Platine** ausschließlich über einen **roten Micromatch-Anschluss**.  

---

### (3) C128/C64 Kernal-Switcher-Platine

<img title="8x Multi-Floppy-Speeder Kernal Switcher C128DCR" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V3.3_U32_Kernal-Switcher-Platine.jpg" alt="loading-ag-2816" style="zoom:25%;" data-align="center">

Die **Kernal-Switcher-Platine** ist eine **Adapterplatine** für ein **512 KB EPROM (27C040 oder 29F040)**, das **acht 64 KB große C128-/C64-Kernal-ROM-Bänke** enthält. Sie wird im **C128DCR** anstelle des originalen **Kernal-PROMs** in den **Sockel (U32)** eingesetzt.  

Der **Switcher** verfügt über einen **Anschluss (J3) für A16/A17/A18**, der mit der **Multi-Speeder-Platine** an **(J5) bzw. (J6)** verbunden werden muss. Die **Multi-Speeder-Platine** schaltet dann neben dem **Kernal des Diskettenlaufwerks** auch die **entsprechende Bank des C128-/C64-Kernal-ROMs** um. Dadurch können das **1571-Kernal** und das **C128-/C64-Kernal** mittels **DOS-Kommandos parallel umgeschaltet** werden. Es werden dabei stets die gleichen **ROM-Bänke** aktiviert.  

- Ist **DOS-Kernal-Bank 0 aktiv**, dann ist auch die **C128-/C64-Kernal-Bank 0 aktiv**.  
- Der **C128-/C64-Teil** erhält jedoch **keinen automatischen Reset**, wie es beim **Diskettenlaufwerk** der Fall ist. Hier ist ein **manueller Reset erforderlich**.  

Wenn **J4** auf dem **Multi-Switcher** geöffnet wird, dann wird das **Diskettenlaufwerk beim Umschalten des DOS-Kernals nicht neu initialisiert (kein Reset).**  

Der **Kernal-Switcher V1.2** (neuere Version, oben) verfügt an **J3** zusätzlich über einen **vierten Anschluss (A15)**. Dieser wird beim **C128DCR nicht genutzt**.  

---

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
Wenn das **1571-Diskettenlaufwerk** im **2-MHz-Modus** läuft (**C128-Modus/DolphinDos**), kann es vorkommen, dass die **ROM-Umschaltung nicht immer zuverlässig funktioniert**. Der **Mikrocontroller ATmega328** hat in diesem Fall **Timing-Probleme** beim **Lesen der Befehle vom Datenbus**.  

Eine zuverlässige Funktion kann erreicht werden, indem der **Quarz Y1** auf der Platine von **20 MHz auf 22,1184 MHz** gewechselt wird. Zwar gibt der Hersteller die **maximale Taktrate** für den **ATmega328P im DIP-Gehäuse** mit **20 MHz** an, jedoch läuft der Mikrocontroller in der Praxis **problemlos mit 22 MHz**.  

---

## Übersicht der C128/C64 und DOS-Kernals

### C128/C64 Kernals U32

Die C128/C64 Kernal-Switcher-Platine für den U32 Sockel ist wie folgt organisiert. Wichtig ist zu beachten, dass derzeit bei dem 512KB EPROM 27C040 und 29F040 immer nur der obere ROM-Bereich 32KB der 64KB Bänke von `$x8000 - $xFFFF` genutzt wird. Somit müssen die Kernals ab `$x8000` platziert werden



Das Kernal ROM 27256 (U32) (C128/C64 Kernals) ist beim C128DCR grundsätzlich wie folgt aufgebaut:

| ROM Adressenbereich | ROM Typ                      |       |
| ------------------- | ---------------------------- | ----- |
| `$0000 - $1FFF`     | C64 Basic V2 `$A000 - $BFFF` | 8KB   |
| `$2000 - $3FFF`     | C64 Kernal  `$E000 - $FFFF`  | 8KB   |
| `$4000 - $7FFF`     | C128 Kernal/System           | 16 KB |

---

### 1571 DOS Kernal (U101 Multi-Speeder)

Das Kernal ROM des Laufwerks beginnt bei `$x3000 - $xFFFF` und je nach aktiver Bank 0-7 wird der entsprechende Bereich dort in den Adressenraum der CPU eingeblendet.



| Bank | Switch  | Eprom Adresse                       | CPU                             |
| ---- | ------- | ----------------------------------- | ------------------------------- |
| 0    | 1@RNROM | `$03000 - $03FFF & $08000 - $0FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |
| 1    | 2@RNROM | `$13000 - $13FFF & $18000 - $1FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |
| 2    | 3@RNROM | `$23000 - $23FFF & $28000 - $2FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |
| 3    | 4@RNROM | `$33000 - $33FFF & $38000 - $3FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |
| 4    | 5@RNROM | `$43000 - $43FFF & $48000 - $4FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |
| 5    | 6@RNROM | `$53000 - $53FFF & $58000 - $5FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |
| 6    | 7@RNROM | `$63000 - $63FFF & $68000 - $6FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |
| 7    | 8@RNROM | `$73000 - $73FFF & $78000 - $7FFFF` | `$3000 - $3FFF & $8000 - $FFFF` |

ROM Bank-Belegung anhand meiner Beispielkonfiguration:

| Bank | Switch  | System            | U32 C128 | U32 C64      | U101 1571    | EPROM                             |
| ---- | ------- | ----------------- | -------- | ------------ | ------------ | --------------------------------- |
| 0    | 1@RNROM | CBM               | CBM      | CBM          | CBM          | `$08000-$0FFFF`                   |
| 1    | 2@RNROM | CBM RAM Exp       | CBM      | CBM          | CBM RAM Exp. | `$18000-$1FFFF`                   |
| 2    | 3@RNROM | DolphinDos 3      | DD3      | DD3          | DD3          | `$28000-$2FFFF`                   |
| 3    | 4@RNROM | DolphinDos 25     | DD3      | DD3-Custom   | DD3          | `$33000 - $33FFF - $38000-$3FFFF` |
| 4    | 5@RNROM | CBM-DD-SD2IEC     | CBM      | DD-JD-SD2IEC | CBM RAM Exp. | `$48000-$4FFFF`                   |
| 5    | 6@RNROM | CBM               | CBM      | JaffyDos 1.3 | CBM RAM Exp. | `$58000-$5FFFF`                   |
| 6    | 7@RNROM | CBM (reserved JD) | CBM      | CBM          | CBM RAM Exp. | `$68000-$6FFFF`                   |
| 7    | 8@RNROM | CBM (reserved JD) | CBM      | CBM          | CBM RAM Exp. | `$78000-$7FFFF`                   |

"CBM RAM Exp." ist das original CBMDOS der 1571 mit einem Patch für die RAM-Erweiterung des Multi-Speeders. Dieser Patch enthält einen TrackCache und so kann das 1571 Diskettenlaufwerk einen kompletten Track auf einmal einlesen. Das JiffyDOS 128 gibt es auch in einer Version mit dem Patch und beschleunigt das lesen nochmal um 20%.



Weitere Informationen dazu auf Github von ytmytm: [GitHub - ytmytm/1571-TrackCacheROM: A firmware patch for Commodore 1571 drive and internal C128D drive enabling RAM expansion use for track cache](https://github.com/ytmytm/1571-TrackCacheROM) 



JiffyDOS 128 läuft perfekt auf dem Multi-Speeder. Besonders mit dem RAM-Expansion Patch ist JiffyDOS im C128 und C64 nochmal erheblich schneller. JiffyDOS habe ich nicht zum Download angeboten, da es noch kommerziell vertrieben wird.



**Bitte beachten das beim Betrieb der Multi-Speeder-Platine das original DOS-ROM U102 ersatzlos herausgenommen werden muss, da der Multi-Speeder jetzt über das eigene EPROM das gewählte DOS-Kernal zur Verfügung stellt! Der Verbleib würde ein Adressenkonflikt erzeugen und das Diskettenlaufwerk würde nicht mehr korrekt funktionieren**



**Beim umschalten kann es Probleme geben, wenn das Diskettenlaufwerk im 2MHz modus betrieben wird. Dann einfach mehrmals z.B. mit (LOAD"x@RNROM",8,1) das gewünschte ROM versuchen umschalten. Das Problem liegt am Timing in Verbindung mit dem ATMega und 74AHTC273 Flip-Flop unter 2MHz. Am besten funktioniert das System mit einem 74AHTC273.** 

---

## Periphal interface Adapter (PIA)

Der Periphal interface Adapter (PIA) steuert die parallele Datenübertragung des Diskettenlaufwerks mit dem C128/C64 über die Parallelport-Adapter-Platine oder einem Parallel Userport Kabel. Getestet habe ich folgende PIA Versionen:

1. **MC68B21P** (Motorola) (2MHz) 
2. **W65C21N6TPG-14** oder **W65C21S6TPG-14** (Western Design Center)   
3. **EF68B21** (STMicroelectronics) (2MHz)
4. **R65C21P2** (Rockwell) (2MHz)

---   

## Diagnosetool

Für den Multi-Speeder-DD3 habe ich ein Programm zu testen des RAM erstellt. Es testet den Zugriff auf das RAM und das RAM Bank-Switching. Das Tool ist für den C64 Modus geschrieben, damit es auf für die C64/1541 Version des Multi-Speeders-DD3 nutzbar ist.  [Link](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/tools)

---

## Benchmark

Hier habe ich einige Benchmarks mit dem 8x Multi-Speeder V2.x erstellt > [[hier]](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/blob/main/benchmark/README.md)

---

## Bill of Materials

Die BOM-Liste steht hier zum Download bereit > [ hier](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/bom) <.

---

### Ein Beispiel für das RAM Bank Switching für Entwickler

Es wäre großartig, wenn sich Entwickler finden, die dabei helfen, das volle **Potenzial des Multi-Speeders** auszuschöpfen.  

Anbei ein **Assembler-Beispiel** für Entwickler, das zeigt, wie die **Speicherbänke des Multi-Speeders** in der **1571** umgeschaltet werden können.  

Der Speicher ist in **vier 8 KB Bänken** unterteilt, die im **Adressbereich `$6000-$7FFF`** in der **1571 eingeblendet** werden.  

Das **Umschalten der Bänke** erfolgt einfach über den **65C21/6821 PIA** mithilfe der **Ports PB0 bis PB5**:  

- **PB0 = A13**,  
- **PB1 = A14**,  
- …  

Standardmäßig sind **PB0 - PB5 auf 0**, sodass **Bank 0 aktiv** ist.



```
LDA #$00           ; PIA DDR for output ($00)
STA $5003          ; Init PIA DDR Port PB0-PB7 output direction
LDA #$FF           ; Set PIA output for Port PB0-PB7
STA $5002          ; Init PIA Port PB0-PB7 aktiv

LDA #$00
STA $5002          ; Set PIA Port PB0-PB1 low        (RAM BANK 0 active)
...
LDA #$01
STA $5002         ; Set PIA Port PB0 high / PB1 low  (RAM BANK 1 active)
...
LDA #$02
STA $5002         ; Set PIA Port PB0 low / PB1 high  (RAM BANK 2 active)
...
LDA #$03
STA $5002         ; Set PIA Port PB0 high / PB1 high (RAM BANK 3 active)`
```

---

## ATMega 328P

Der Atmel ATMega 328P Microcontroller überwacht den Datenbus und steuert die ROM-Bänke und ist für den Wechsel der Betriebsmodi zuständig. Die Firmware kann über ein Arduino Board oder einen AV Programmer programmiert werden. Ich nutze den XGecu T48 Universal Programmer über eine .mpj Projektdatei. Beim programmieren mit dem XGecu mit der .mpj Datei bitte das EEPROM nicht mit programmieren, da es sonst eine Fehlermeldung gibt. Dieses kann man im Menü des XGecu deaktivieren.

<img title="" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/XGecuT48UniversalProgrammerEEPROM.png" alt="" data-align="center" style="zoom:25%;">

<img title="" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/XGecuT48UniversalProgrammerConfig.png" alt="" style="zoom:25%;" data-align="center">

## Installation C128DCR

<img title="8x Multi-Speeder Install C128DCR  Mainboard" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V2.0_C128DCR_Overview.jpg" alt="8x Multi-Speeder Install C128DCR  Mainboard" style="zoom:50%;" data-align="center">

Die Installation des Multi-Speeders auf dem C128DCR Mainboard. Der Multi-Speeder wird anstelle der 6502 CPU (U101) eingesetzt. Die 6502 CPU wird auf den CPU-Sockel des Multi-Speeder gesetzt (unten rechts). Der Kernal-Switcher befindet sich unten links und wird anstelle des original Kernals auf den Sockel (U32) gesetzt. Der Parallel-Adapter kommt anstelle des CIA 6526 (U4) in einen Sockel. Der CIA 6526 wird auf den Parallel-Adapter-Platine gesetzt. Der Kernel-Switcher wird mit einem drei PIN Kabel mit dem Multi-Speeder verbunden. Der Parallel-Adapter wird mit einen 10 poligen Kabel ebenfalls mit der Multi-Speeder-Platine verbunden (Parallelport).

---

## Downloads

1. [ATF16V8 (GAL16V8) Dateien](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/pld-atf16v8-gal16v8)

2. [ATMEL ATMega328 P Dateien](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/atmega328p)

3. [Gerber-Dateien zur Platinenherstellung](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/gerber)

4. [Firmeware / Kernals](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/kernals)

5. [Schaltpläne zum 8x Multi-Speeder](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/schematics)

6. [Fotogalerie](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/images)

7. [Weitere Dokumente](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/tree/main/docs)

---   

## Shared Projects auf PCBWay.com

1. [8x Multi-Floppy Speeder 32KB RAM Expansion für den Commodore C128DCR](https://www.pcbway.com/project/shareproject/Switchless_8x_Multi_Floppy_Speeder_with_32_KB_RAM_Expansion_for_the_Commodore_C1_557a83c8.html)

2. [C128/C64 Kernal-Switcher für 8x Multi-Floppy-Speeder C128DCR](https://www.pcbway.com/project/shareproject/C128_C64_U32_Kernal_Switcher_Adapter_for_Switchless_8x_Multi_Floppy_Speeder_with_f113e895.html)

3. [Parallel-Port-Adapter für 8x Multi-Floppy-Speeder C128DCR](https://www.pcbway.com/project/shareproject/Parallelport_Adapter_U4_for_Switchless_8x_Multi_Floppy_Speeder_with_32_KB_RAM_Ex_558623e7.html)

---   

### Weitere Projekte auf PCBWay.com:

### Commodore 1541 Switchless 8x Multi-Speeder

1. [Switchless Floppy Drive 8x Multi Floppy Speeder (THT) for the Commodore 1541 Disk Drive (V2.2c)](https://www.pcbway.com/project/shareproject/Switchless_Floppy_Drive_8x_Multi_Floppy_Speeder_for_the_Commodore_1541_Disk_Driv_369dbba4.html)

2. [Switchless Floppy Drive 8x Multi Floppy Speeder (SMD) for the Commodore 1541 Disk Drive (V2.2c)](https://www.pcbway.com/project/shareproject/Switchless_Floppy_Drive_8x_Multi_Floppy_Speeder_for_the_Commodore_1541_Disk_Driv_33eedf94.html)

3. [Parallel Cable Sets for the Commodore 1541 Disk Drive (SpeedDOS, DolphinDOS) with the C64/C128](https://www.pcbway.com/project/shareproject/C64_Userport_Adapter_Parallel_Cable_Set_for_the_Commodore_1541_Disk_Drive_Spe_3b86d1f8.html)

### Commodore 1541 Parallel Port Adapter VIA 6522

1. [1541-I/1541-II Parallel Adapter (Duo/Slim) - Parallel Cable Set for the Commodore 1541 Disk Drive (SpeedDOS, DolphinDOS) with the C64/C128](https://www.pcbway.com/project/shareproject/1541_I_1541_II_Parallel_Adapter_Duo_Slim_Parallel_Cable_Set_for_the_Commodor_57072954.html)

2. [1541-I/1541C Parallel Adapter - Parallel Cable Set for the Commodore 1541 Disk Drive (SpeedDOS, DolphinDOS) with the C64/C128](https://www.pcbway.com/project/shareproject/1541_I_1541C_Parallel_Adapter_Parallel_Cable_Set_for_the_Commodore_1541_Disk_D_a27176a6.html)

3. [C64 User Port Adapter - Parallel Cable Set for the Commodore 1541 Disk Drive (SpeedDOS, DolphinDOS) with the C64/C128](https://www.pcbway.com/project/shareproject/C64_Userport_Adapter_Parallel_Cable_Set_for_the_Commodore_1541_Disk_Drive_Spe_3b86d1f8.html)

---   

## Hilfreiche Links

1. DolphinDos [Dolphin DOS – C64-Wiki](https://www.c64-wiki.de/wiki/Dolphin_DOS) & https://project64.c64.org/hw/dolphindos.txt

2. RAMBoard: [RAMBOard – C64-Wiki](https://www.c64-wiki.de/wiki/RAMBOard) & [https://www.c64copyprotection.com/ramboard/](https://www.c64copyprotection.com/ramboard/) & [[CSDb] - Super-Card 6 Plus RAMboard [scpu] by Master (2018)

---   

## Danke

Zu diesem Projekt haben viele beigetragen und ist das Ergebnis vieler Entwickler. Besonders möchte ich mich bei folgenden Entwicker bedanken.

1. Jan Bubela und Gunther Jilg die DolphinDos entwickelt haben.

2. RetroNynjah hat mir geholfen seinen Switchless Multi-ROM auf den 8x Multi-Speeder zu integrieren. [GitHub - RetroNynjah/Switchless-Multi-ROM-for-27128-27256](https://github.com/RetroNynjah/Switchless-Multi-ROM-for-27128-27256)

3. **Jim Drew and Joeri van Haren**, für Hilfe und für die Review-Version 2.1 by Jim Drew

4. Die hilfreiche Seite mit technischen Daten zu DD3 von silverdr. [https://e4aws.silverdr.com/projects/dolphindos3/](https://e4aws.silverdr.com/projects/dolphindos3/)

5. Ytmytm für seinen TrackCache: [GitHub - ytmytm/1571-TrackCacheROM: A firmware patch for Commodore 1571 drive and internal C128D drive enabling RAM expansion use for track cache](https://github.com/ytmytm/1571-TrackCacheROM)

6. Stefan Kauf für seine Unterstützung bei der Idee des Mult-Speeders und seinen Vorlagen.

---   

## Haftungsausschluß

Ich habe dieses Projekt mit großer Sorgfalt gestaltet und getestet. Aber Fehler können immer passieren. Dieses Projekt ist ein Hobbyprojekt. Ich übernehme deshalb keine Garantie für die Funktion oder für etwaige Schäden, die durch den Einbau oder die Nutzung dieses Projektes in jeglicher Art entstehen könnten.

---

## Spenden

Ich habe viele Stunden an diesem Projekt gearbeitet. Wenn Du diese Arbeit unterstützen möchtest, dann kannst Du mir etwas für die Kaffekasse spenden. Vielen Dank! [Paypal Spende hier klicken!](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=Q8HXKYARXKT4L&ssrt=1714757590172)

---

## Nutzungsrecht / Copyright

Du kannst diese Projekt gerne für private zwecke nutzen. Die kommerzielle Nutzung wie z.B. Verkauf oder andere Verbreitung meines Multi-Floppy-Speeders ist ohne meine Erlaubnis untersagt.



Ich wünsche euch viel Freude mit meinem 8x Multi-Floppy-Speeder 32KB RAM Expansion für den C128D CR.



Viele Grüße
Frank Eggen 

E-Mail: [retro@emden.net](mailto:retro@emden.net)

---

## Update

- 2025-03-08 Neue Version 3,3 mit 512KB RAM und DolphinDos 25
- 2025-01-02 Hinzu weitere Links zum 1541 8x Switchless Multi-Speeder 32KB
- 2024-12-07 PCB-Gerberdatei Update auf Version 2.0b - Fehler R2 und R3 bereinigt. Zwischen Pull-Up-Widerständen R2-R3 müssen 5V anliegen.
