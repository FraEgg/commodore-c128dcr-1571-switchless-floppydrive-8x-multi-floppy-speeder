# Switchless 8x Multi-Floppy Speeder with 32 KB RAM Expansion for the Commodore C128 DCR and Internal 1571 Floppy Drive (DolphinDOS 3 Compatible)

## Multi-Speeder DD3 RAM Diagnistic-Tool

![Multi-Speeder-Diagnistic](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/blob/main/images/multi-speeder-dd3-diag1.png?raw=true "Multi-Speeder-Diagnistic")



### Description

The Multi-Speeder Diagnostic Tool checks the RAM function of the speeder. A stable RAM function is important so that the speeders that require additional RAM also function reliably.

The Multi-Speeder DD3 has 32KB RAM available in four banks. The RAM banks are embedded as 8KB banks in the memory area` $6000-$7FFFF ` of the 1571 diskette drive. The banks are switched by the PIA at ports PB0 and PB1.

The Diagnistic-Tool checks whether the bank switching via the PIA works. The RAM area Bank 0 - Bank 3 is then checked with write and read accesses. 

I recommend starting the diagnostic tool with the original CBMDOS on ROM bank 0 (`@I:1@RNROM`). Otherwise it could happen that a speeder comes into conflict with the write accesses with the diagnostic tool and errors occur during the RAM test.



![RAM Test](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/blob/main/images/multi-speeder-dd3-diag2.png?raw=true "RAM Test")

The Diagnistic-Tool tests every bank.



![Test ended](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/blob/main/images/multi-speeder-dd3-diag3.png?raw=true "Test ended")

The RAM was tested successfully.



![no bankswitching](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder/blob/main/images/multi-speeder-dd3-diag4.png?raw=true "no bankswitching")

The bank switching failed here. The jumpers A14RAM and A15RAM may be open. In this case, insert a solder bridge for these jumpers on the back of the Multi-Speeder board. Alternatively, there is only one 8K RAM on the board or the PIA does not switch the banks. If the bank switching does not work, the diagnostic tool tests the 8K RAM at `$6000-$7FFF` of the memory in the 1571 floppy disk drive.



### Example of ram bank switching for developers

To switch the memory banks, proceed as follows:

```
LDA #$00           ; PIA DDR for output ($00)
STA $5003          ; Init PIA DDR Port PB0-PB7 output direction
LDA #$FF           ; Set PIA output for Port PB0-PB7
STA $5002          ; Init PIA Port PB0-PB7 aktiv

LDA #$00
STA $5002          ; Set PIA Port PB0-PB1 low         (RAM BANK 0 active)
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



Best regards,  
Frank Eggen
