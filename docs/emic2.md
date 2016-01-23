# Emic2 Driver

## `zorg_emic.Emic2`

## Methods

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

## `pause()`

Calling this method will immediately pause current message.

## `stop()`

Calling this method will immediately stop the current message from being spoken.

## `reset()`

Calling this method will reset the current message that is beign spoken.
