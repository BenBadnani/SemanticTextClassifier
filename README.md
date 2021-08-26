# SemanticTextClassifier

**Version 1.0.0**

A text classification program that highlights which of the two inputted source text models, the body of text most in question most resembles semantically.

## Usage

Run the python script in terminal:

```terminal
$ python finalproject.py
```

Define and add your two source text models in the directory and then define the third model based on the mystery text.
Then run the classify method on the objects.

```python
source1 = TextModel('Shakespeare')
source1.add_file('Shakespeare.txt')

source2 = TextModel('Whitman')
source2.add_file('Whitman.txt')

new1 = TextModel('Twain')
new1.add_file('Twain.txt')
new1.classify(source1, source2)
```

## Tests

In the python shell, run

```python
>>> run_tests()
```

Output: 

```
scores for Shakespeare: [-17133284.93897174, -5898871.3141015945, -16900213.927793667, -576973.3267420715, -945555.8702132187]
scores for Whitman: [-15764654.49053656, -5811033.803917469, -16038888.914171463, -541114.9437922955, -882368.5125352446]
Twain is more likely to have come from Whitman
scores for Shakespeare: [-5707.013588921243, -1691.8431657789718, -5456.800535538245, -148.211499476162, -189.3238673923349]
scores for Whitman: [-4997.925359142177, -1651.0997465455937, -4885.818590250593, -138.5890912442551, -201.86306108013014]
CNN is more likely to have come from Whitman
scores for Shakespeare: [-4259.14757996746, -1401.5659851044184, -4045.8957702565413, -105.26665252353531, -231.85192977192753]
scores for Whitman: [-3932.724809803094, -1364.5073533584318, -3754.8914015135956, -91.58535790305521, -182.0482633231169]
ScienceDaily is more likely to have come from Whitman
scores for Shakespeare: [-50150.59083920933, -14635.04646160747, -48056.57744110053, -1510.4628300882862, -1742.374607553585]
scores for Whitman: [-46871.49314628835, -14504.717379935371, -45949.93864016276, -1399.061750740481, -1583.9989474229146]
ESPN is more likely to have come from Whitman
```

## Authors and acknowledgment

Ben Badnani, <bbadnani@bu.edu>
Brad Schulman, <brad217@bu.edu>
