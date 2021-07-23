
# Wang-Mendel

This is an implementation of the Wang-Mendel algorithm to learn a fuzzy 
rule base from data.


Original paper: https://ieeexplore.ieee.org/document/199466


For a Portuguese brief explanation of the algorithm: https://github.com/renatolm/wang-mendel/blob/master/Slides.pdf
## Installation

The project was designed in Python 3.6.9, but may work fine on other
versions of Python 3.6+ as well.

To install all the requirements, just type on terminal:

```bash
  pip install -r requirements.txt
```
    
## Usage/Examples

#### <u>Basic usage</u>:

The first step is to learn the raw fuzzy rule base
```python
n_regions_inputs = [4,4,4,4]            # optional: how many fuzzy regions for each input variable
n_regions_output = 2                    # optional: how many fuzzy regions for the output variable
name_preffix_inputs = ['A','B','C','D'] # optional: the names of each input variable
name_preffix_output = 'E'               # optional: the name of the output variable

rule_base = wangmendel.learn_fuzzy_rules(X_train, y_train,
                                        n_regions_inputs=n_regions_inputs,
                                        n_regions_output=n_regions_output,
                                        name_preffix_inputs=name_preffix_inputs,
                                        name_preffix_output=name_preffix_output)
```

Then, the next step is to clean the rule base of contradicting rules    
```python
rule_base = wangmendel.clean_rule_base(rule_base)
```

And finally to make predictions for a crisp input. The output is a fuzzy set (y: domain, f_y: image).
```python
y, f_y = mamdani.predict_crisp(x, rule_base)
```
Since the output is a fuzzy set, you may want to "defuzzify" the result
to get a number.
```python
defuzz.centroid(y, f_y)
```


#### <u>Examples</u>:
For a more detailed regression example (predicting the Mackey-Glass series): https://github.com/renatolm/wang-mendel/blob/master/Examples/Mackey-Glass/Mackey-Glass.ipynb

For a classification example (predicting Blood donations): https://github.com/renatolm/wang-mendel/blob/master/Examples/Blood/Blood.ipynb




## Roadmap

- Add support to fuzzy inputs

- Create tests!

- Turn the project into a package and publish on PyPI
