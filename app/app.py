import sys,subprocess,json

def handler(event, context):
    print("Received event: " + json.dumps(event, indent = 4))
    payload = json.loads(event['body'])
    switch_dict = {
        "sum": handle_sum,
        "triangle-area": handle_triangle_area
    }
    func = switch_dict.get(payload.get('operation', None), handle_unsupported_operation)
    result = func(payload)
    return result

def handle_sum(event):
    my_data = event['a'] + ',' + event['b'] + ',' + event['c']

    process = subprocess.run(["./sum"], universal_newlines=True, input=my_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    print(process)
    if process.returncode == 0:
        output = process.stdout.split(" ")[-1].replace("\n","")
        return result(output)
    else:
        return error()

def handle_triangle_area(event):
    my_data = event['a'] + ',' + event['b'] + ',' + event['c']

    process = subprocess.run(["./triangle-area"], universal_newlines=True, input=my_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    print(process)
    if process.returncode == 0:
        output = process.stdout.split(" ")[-1].replace("\n","")
        return result(output)
    else:
        return error()

def handle_unsupported_operation(event):
    return {
        'statusCode': '400',
        'body': json.dumps({"message": "Unsupported Operation"}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def result(result):
    return {
        'statusCode': '200',
        'body': json.dumps({"result": result}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def error():
    return {
        'statusCode': '500',
        'body': json.dumps({"message": "Generic Error"}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }
