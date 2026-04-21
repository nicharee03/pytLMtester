This method is based on pynguin0.19, and you can run pytLMTester just like running pynguin

# Setup Guide: pytLMtester

These instructions assume you are already inside the **Turing project** and the `pytLMtester` submodule is present.

---

## 1. Requirements

- Python **3.10**
- Pynguin **0.19.0**

---

## 2. Initialise Submodule 

```bash
git submodule update --init --recursive
```

---

## 3. Navigate to pytLMtester

```bash
cd pytLMtester
```

---

## 4. Create and Activate Virtual Environment

### Windows (CMD)
```bash
py -3.10 -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux
```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r pytlm/requirements.txt
```

---

## 6. Set Required Environment Variable

### Windows
```bash
set PYNGUIN_DANGER_AWARE=1
```

### macOS/Linux
```bash
export PYNGUIN_DANGER_AWARE=1
```

---

## 7. Run pytLMtester

```bash
python -m pytlm --project-path <path-to-target-folder> --output-path <output-folder> --module-name <module-name-without-.py> -v
```

### Example

```bash
python -m pytlm --project-path ./docs/source/_static --output-path ./pynguin-results --module-name queue_example -v
```

---

## 8. Run Generated Tests

### Windows
```bash
set PYTHONPATH=.\docs\source\_static
```

### macOS/Linux
```bash
export PYTHONPATH=./docs/source/_static
```

```bash
pytest ./pynguin-results -v
```

---

## Notes

- Generated tests are saved in `pynguin-results/`
- Files with `_failing` contain tests that raised exceptions during generation

---