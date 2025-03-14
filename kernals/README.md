# Switchless 8x Multi-Floppy-Speeder V3.3 with 512 KB RAM expansion for the Commodore C128 DCR and the internal 1571 floppy drive (DolphinDOS 3 / new DolphinDOS 25)

## C128/C64 and 1571 Test-Kernels

<img title="8x Multi-Floppy-Speeder Kernal Switcher C128DCR" src="https://raw.githubusercontent.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/refs/heads/main/images/V3.3_U32_Kernal-Switcher-Platine.jpg" alt="loading-ag-280" style="zoom:25%;" data-align="center">

Here I have prepared two EPROMs for the Multi-Speeder and the C128/C64 U32 Kernal-Switcher. 

This contains the DolphinDos 3/DolphinDos 25 and the original CBM-DOS. 



JiffyDOS can be added by each owner himself. Since JiffyDOS is still being marketed, I do not include it in the ROMs for copyright reasons.

1. Kernals for internal 1571 (Multi-Speeder PCB): [1571-U101-Multi-Speeder-29F040-CBM-CBM-DD3-DD25-SD2IEC-RAM-Patch.BIN](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/raw/refs/heads/main/kernals/1571-U101-Multi-Speeder-29F040-CBM-CBM-DD3-DD25-SD2IEC-RAM-Patch.BIN)

2. Kernals for C128/C64 U32 (Kernal-Switcher PCB): [C128-U32-Kernal-Switcher-29F040-CBM-CBM-DolphinDos3-SD2IEC-RAM-Patch.BIN](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/raw/refs/heads/main/kernals/C128-U32-Kernal-Switcher-29F040-CBM-CBM-DolphinDos3-SD2IEC-RAM-Patch.BIN)
   
   

On the new Kernal-Switcher PCB above v1.2 the Adressline A15 is unused on J3. 

---

# ROM Organization

The firmware (kernels) for the 1571 floppy drive and C128/C64 are stored in a 512 KB EPROM of type 27C040 or 29F040 (PLCC32) and organized into 8x 64 KB banks. Each bank (0–7) represents the complete 64 KB address range.

---

## Internal 1571 Floppy Drive

The address decoder of the Multi-Speeder Board maps the ROM in the floppy drive to the address range `$8000 to $FFFF`.

**Please note:** When operating the Multi-Speeder Board, the original DOS-ROM U102 must be removed entirely, as the Multi-Speeder now provides the selected DOS kernel via its own EPROM! Leaving the original ROM in place would create an address conflict, causing the floppy drive to malfunction.



Here is the configuration of the example kernals:

| Bank  | Switch  | System            | U32 C128 | U32 C64        | U101 1571    | EPROM                          |
| ----- | ------- | ----------------- | -------- | -------------- | ------------ | ------------------------------ |
| 0     | 1@RNROM | CBM               | CBM      | CBM            | CBM          | `$08000-$0FFFF`                |
| 1     | 2@RNROM | CBM RAM Exp       | CBM      | CBM            | CBM RAM Exp. | `$18000-$1FFFF`                |
| 2     | 3@RNROM | DolphinDos 3      | DD3      | DD3            | DD3          | `$28000-$2FFFF`                |
| **3** | 4@RNROM | **DolphinDos 25** | **DD3**  | **DD3-Custom** | **DD25 B1**  | `$33000-§3FFF & $38000-$3FFFF` |
| 4     | 5@RNROM | CBM-DD-SD2IEC     | CBM      | DD-JD-SD2IEC   | CBM RAM Exp. | `$48000-$4FFFF`                |
| 5     | 6@RNROM | CBM               | CBM      | JaffyDos 1.3   | CBM RAM Exp. | `$58000-$5FFFF`                |
| 6     | 7@RNROM | CBM (reserved JD) | CBM      | CBM            | CBM RAM Exp. | `$68000-$6FFFF`                |
| 7     | 8@RNROM | CBM (reserved JD) | CBM      | CBM            | CBM RAM Exp. | `$78000-$7FFFF`                |

## Note Bank 3 DolphinDos 25 B1:

**Bank 3 (4@RNROM**) contains my modified DolphinDos 25 B1 (Beta1). This DOS is based on 1571 DolphinDos 3 and is extended by a internal disk copy routine. This can save a complete floppy disk page to the internal 512KB RAM in one read operation and write it back to a formatted floppy disk.

New DOS - Commands:

@CDR1        (Read a disk page to memory 1)
@CDW1       (Write memory 1 back to a formatted floppy disk)

@CDR2        (Read a floppy disk page in memory 1)
@CDW2        (Write memory 1 back to a formatted floppy disk)



Memory 1 and 2 are retained until the floppy disk drive is switched off or the memory is overwritten with the copy routine.

---

## C128/C64 Kernels

The kernel ROM 27256 (U32) in the C128DCR is structured as follows:

| ROM Address Range | ROM Type                     | CPU Address Range |
| ----------------- | ---------------------------- | ----------------- |
| `$0000 - $1FFF`   | C64 Basic V2 `$A000 - $BFFF` | 8 KB              |
| `$2000 - $3FFF`   | C64 Kernel `$E000 - $FFFF`   | 8 KB              |
| `$4000 - $7FFF`   | C128 Kernel/System           | 16 KB             |



The C128/C64 Kernel Switcher Board for the U32 socket is organized as follows. It is important to note that, for the 512 KB EPROM (27C040 and 29F040), only the upper 32 KB of the 64 KB banks (`$x8000 - $xFFFF`) are currently used. Therefore, the kernels must be placed starting at `$x8000`.



Best regards,  
Frank Eggen
