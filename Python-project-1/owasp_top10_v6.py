# Vulnerable code using an outdated and vulnerable version of a package

import flask

print(f"Flask version: {flask.__version__}")

@app.route('/safe')
def safe_endpoint():
    return 'This is safe.'

if __name__ == '__main__':
    app.run()