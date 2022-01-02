# Exeter Challenge

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Friendly challenge for my fellow exonians.

## Table of Contents

- [Challenge Explanation](#challenge_explanation)
- [Project Structure](project_structure)
- [Licence](#licence)

### Challenge Explanation

#### Pre Challenge Stage
Before one can even start solving the puzzle they must pass this stage. To gain access to the rest of the challenge on must download the image and open it like a text file. At the very bottom of the page there is a link to the challenge as well as the ciphertext and hints for the next challenge.

#### Stage 1: Overcome the Hill
Along with the hints left in the image the title of the stage was also a hint. The cipher text was ciphered with the [Hill Cipher](https://en.wikipedia.org/wiki/Hill_cipher). The decryption matrix was written at the bottom of the file making this a simple stage to pass.

#### Stage 2: Spiral Into Madness
Similar to [stage 1](#stage_1) the title was a hint. The cipher text was ciphered with the [Sprial Cipher](https://en.wikipedia.org/wiki/Transposition_cipher). This time no key was provided as it is not very difficult to brute force the spiral cipher.

#### Stage 3: No Hints
As the title suggested no hints were provided in this stage. To make up for the lack of hints the cipher that was used was very easy to crack once identified. The cipher text was ciphered with the [Caeser Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). This cipher could be cracked using frequency analysis or by brute force. The intended method was brute force as the text was not long enough for frequency analysis to be effective and the token is completely random.

#### Stage 4: Custom Cipher
This cipher has no key. The only way to crack it is using frequency analysis. The cipher is a mono-alphabetic cipher similar to the [Caeser Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). The major difference between this cipher and the Caeser Cipher is that the mapping between letters in the cipher is random. The ciphertext was generated using [cipher.py](src/cipher.py).

#### Stage 5: Final Stage
This stage was going to be called "Layers" but I wanted it to be apparent that this was the final stage. This is by far the most challenging cipher. Pluging the ciphertext into any sort of cipher analyzing tool gived inconclusive results. This stage is unique as the cipher text was ciphered with 4 ciphers with short messages mixed in. A hidden hint in the page is the key to the first layer displayed on the screen in white text.

- **Layer 1**:
The first layer was ciphered with the [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), the alphabet and key were given in the white text on the page.

- **Layer 2**:
The second layer was ciphered with the [Rail Fence Cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher), a hint was left hinting that the railfence cipher was used and the railfence cipher is fairly straightforward to brute force.

- **Layer 3**:
The third layer was ciphered with the [Caeser Shift](https://en.wikipedia.org/wiki/Caesar_cipher).

- **Layer 4**:
The final layer was not ciphered but rather encrypted with [RSA Encryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). The numerical form of the ciphertext was left in and the minimum amount of information to decrypt it was left.

Once All 4 stages were cracked the challenger is left with the final token

#### Congrats
The final page of the challenge doesn't have any ciphers but instead is a congradulations page.

### Project Structure

| Name                 | Description                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| **package.json**     | Has all of the package requirements and node configurations                |
| **Procfile**         | Config file for [heroku](https://www.heroku.com)                           |
| **LICENSE**          | Holds license for challenge                                                |
| **.gitignore**       | Standard gitignore file to prevent unwanted files form being commited      |
| **.prettierrc**      | Config file for prettier                                                   |
| **src/app.js**       | Runs challenge website                                                     |
| **src/cipher.py**    | Standalone script to generate cipher for [stage 4](views/stage-4.html)     |
| **views**            | All of the HTML files for the project are housed here                      |

### Licence

Licenced under the [MIT](LICENSE) License

Copyright (c) 2021 Altan Mehmet Ünver (L0ad1n6)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
