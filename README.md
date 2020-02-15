
# Identity Generator
## Idea
**WORK IN PROGRESS** <br>
Generate a random and plausible fake identity, currently German identities only.
The identity can be exported as `.json` file or directly used as a `python dictionary`.


## Usuage
**CURRENTLY:** <br>
Since the project is still in dev, I do not provide a package yet.
You need to have the `generator.py` file in the same directory as your file and keep the folder structure. 
```python
from generator import Generator

gen = Generator()
# generate new identity
gen.genIdentity()
# print the generated identity
gen.identity.print()
# get python dict
gen.identity.getAsDict()
# get identity as json
gen.identity.json()
```

## Disclaimer
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to the [LICENSE](LICENSE) or <https://unlicense.org>
