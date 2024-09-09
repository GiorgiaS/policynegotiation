# Policy Negotiation for Human Digital Twins in multi-user/provider scenario

This is the official repository storing the implementation of the paper: "Efficient Enforcement of Privacy Preferences for Human Digital Twins in Multi-User/Provider Scenarios".

```
@inproceedings{sirigu2024human,
  title={Efficient Enforcement of Privacy Preferences for Human Digital Twins in Multi-User/Provider Scenarios},
  author={Sirigu, Giorgia and Carminati, Barbara and Ferrari, Elena},
  ...
}
```

## Requirements
- Python 3.10+[^1]
- Python libraries: see file `requirements.txt`

## Run the System
1. Modify the number of policies and privacy preferences in `IntermediatePolicy.py` file from `16` to `19` of the processes of interest to test.
2. Run file `IntermediatePolicy.py`
3. Results will be stored into the `output` folder

## Results
Results are organised in _.xlsx_ files generated in the main directory.
Results of the single processes are stored within the `results` folder

[^1]: https://www.python.org/
