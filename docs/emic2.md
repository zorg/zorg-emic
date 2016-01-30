# Emic2 Driver

## `zorg_emic.Emic2`

The Zorg Emic 2 Driver provides a convenient software interface for controlling
the Emic 2 text to speech module.

## Commands

Various commands are available which provide access to the various features of
the Emic 2 module.

## `start()`

The `start` method establishes a connection to the host.
If you are using the `zorg_emic.Serial` adaptor, then
this method will set up the serial connection between
your device and the emic2 text to speech module.

## `speak(text)`

The `speak` method takes the text to be spoken as a parameter.

## `set_voice(voice)`

The `set_voice` method takes a single integer paramter.
This integer corresponds to one of the nine voices that
are supported by the board.

The options are...

0. Perfect Paul (Paulo)
1. Huge Harry (Francisco)
2. Beautiful Betty
3. Uppity Ursula
4. Doctor Dennis (Enrique)
5. Kit the Kid
6. Frail Frank
7. Rough Rita
8. Whispering Wendy (Beatriz)

## `set_language(language, dialect=None)`

The `set_language` method sets the language to be used for the text to speech process.

The language options that can be passed in are

1. `"en"` (English)
2. `"es"` (Spanish)

If you are using the Spanish option (`"es"`), then you can also pass in an additional parameter for the dialect.
By default, the dialect is latino, but a value of `"ca"` can be specified for castilian. 

## `set_volume(volume)`

Set the volume of the by passing in a parameter between -48 and 18. (-48 is the softest and 18 is the loudest).

## `set_rate(rate)`
This method sets the speaking rate in words per minute.
The possible values range from 75 which is the slowest to 600 which is the fastest.

By default, the speaking rate of the board is set to 200.

## `set_parser(parser)`

The Emic 2 provides a choice of text parsing engines: Epson or DECtalk.
Both parsers provide different levels of control over the output of a given string.

The parser can be selected by passing in an integer to select the corresponding parser.

- `0` DECtalk
- `1` Epson (default)

### Epson Parser

The Epson parser allows dynamic changes of emphasis, pitch, voice selection,
and speaking rate to take place within a text using embedded mark-up control symbols:

- `\/` Decrease pitch
- `/\` Increase pitch
- `>>` Increase speaking rate
- `<<` Decrease speaking rate
- `__` Emphasize the next word

An example of these commands being used to dynamically change the characteristics of the speech:

> :-)0 Hello everyone. My name is Emic 2. I am the next generation text-to-speech module created by Grand Idea Studio. I can ##whisper ##very ##quietly. I can change to 1 of 9 voices. For example, from Paul :-)1 to Harry :-)4 to Dennis :-)8 to Wendy. :-)0 I can also /\/\ increase my pitch. /\/\ And increase my pitch again. >>>> Then speak faster >>>> and even faster >>>> and even faster again. <<<<<<<<<<<< \/\/\/\/ And then go back to normal.

### DECtalk Parser

The DECtalk parser is intended for advanced users and allows the finest control and customization of
speech output by providing direct access to the internal parameters of the DECtalk 5.0.E1 text-to-speech
synthesizer engine.

The DECtalk commands supported by the Emic 2 Text-to-Speech Module consist of the following:

- `[:comma]` Set the length of a comma pause (in milliseconds)
- `[:dv]` Customize voice parameters (save option not supported)
- `[:mode]` Set how text is processed/parsed (no e-mail parsing supported)
- `[:name]` Set the current speaking voice (numbers only: 0-8)
- `[:period]` Set the length of a period pause (in milliseconds)
- `[:phoneme]` Enable phonemic interpretation of subsequent text
- `[:pitch]` Modify the pitch of uppercase letters
- `[:pronounce]` Set the type of pronunciation for the subsequent word
- `[:punct]` Set how punctuation marks are handled
- `[:rate]` Set speaking rate
- `[:say]` Specify when speaking begins
- `[:skip]` Skip a selected part of text pre-processing
- `[:sync]` Makes a command synchronous to allow it to be processed before synthesis continues

An example of these commands being used to dynamically change the characteristics of the speech:

> [:rate 200][:n0][:dv ap 90 pr 0] All your base are belong to us.

## `pause()`

Calling this method will immediately pause current message.

## `stop()`

Calling this method will immediately stop the current message from being spoken.

## `reset()`

Calling this method will reset the current message that is beign spoken.
