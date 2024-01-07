# VigilantEye-Worker

VigilantEye is a Python web scanning toolkit built with Flask, featuring a master and worker architecture. It enables users to perform various scans using both built-in modules and custom modules added to the `MODULES` folder.

## Master
[https://github.com/stephanevdb/VigilantEye-Master](https://github.com/stephanevdb/VigilantEye-Master)

## Getting Started

### Prerequisites

- Python (3.11 or higher)
- Communication between master and worker on ports `8666` and `8667`
- A running master node

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Worker:

```bash
python app.py
```





## License

[GPL License](LICENSE).