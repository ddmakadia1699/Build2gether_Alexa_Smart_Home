import paho.mqtt.client as mqtt
import logging
import time
from datetime import datetime
import json
import uuid
import requests
import random
import colorsys
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


# Imports for v3 validation
from validation import validate_message

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
def on_connect(client, userdata, flags, rc) :
    print ("Connected!", str(rc))

def lambda_handler(request, context):
    global names
    """Main Lambda handler.

    Since you can expect both v2 and v3 directives for a period of time during the migration
    and transition of your existing users, this main Lambda handler must be modified to support
    both v2 and v3 requests.
    """
    mqtt_broker_ip = "tailor.cloudmqtt.com"
    client = mqtt.Client("cloudmqtt"  + str(random.randint(1,1000)))
    client.username_pw_set("ffbqwwfa","PAC8F72zynig")
    client.on_connect = on_connect
    client.connect(mqtt_broker_ip, 13582)
    #client.publish("test",str(request))
    print ("Connected")
    print (str(request))
    version = get_directive_version(request)
    print (version)
    try:
        logger.info("Directive:")
        logger.info(json.dumps(request, indent=4, sort_keys=True))

        version = get_directive_version(request)
        
        if version == "3":
            print ("version ")
            logger.info("Received v3 directive!")
            
            if request["directive"]["header"]["name"] == "Discover":
                print ("working")
                # client = boto3.client('dynamodb')
                # DB =     boto3.resource('dynamodb')
                # table = DB.Table('device')
                # response = table.update_item(
                #     Key={
                #         'api_key': 'v5'
                #     },
                #     UpdateExpression="set statusTemp=:t",
                #     ExpressionAttributeValues={
                #         ':t': "9.99"
                #     },
                #     ReturnValues="UPDATED_NEW"
                # )
                mqtt_broker_ip = "tailor.cloudmqtt.com"
                client = mqtt.Client("cloudmqtt"  + str(random.randint(1,1000)))
                client.username_pw_set("ffbqwwfa","PAC8F72zynig")
                client.on_connect = on_connect
                client.connect(mqtt_broker_ip, 13582)
                # client.publish("test",str(r.text))
                client.publish("test","test")
                client.loop_start()
                client.loop_stop()
                print("Discovery done")
                #temp = request["directive"]["payload"]["scope"]["token"]
                #userid = temp[0]
                #print(userid)
                #user = str(userid)
                user = '4'
                client = boto3.client('dynamodb')
                DB =     boto3.resource('dynamodb')
                table = DB.Table('device')
                response = table.scan(
                    FilterExpression=Attr('user').eq(user)
                )
                items = response['Items']
                #print (items)
                print (len(items))
                end =  '{"endpoints" : []}'
                yx = json.loads(end)
                temp12 = yx['endpoints'] 
                for a in range(len(items)):
                    endpointId = items[a]['api_key']
                    displayCategories = items[a]['displayCategories']
                    description = items[a]['description']
                    friendlyName = items[a]['friendlyName']
                    manufacturerName = "Dhrumil_Makadia"
                    cap =  '{"capabilities" : []}'
                    y = json.loads(cap)
                    temp = y['capabilities'] 
                    BrightnessController = '{"type": "AlexaInterface","interface": "Alexa.BrightnessController","version": "3","properties": {"supported": [{"name": "brightness"}],"proactivelyReported": true,"retrievable": true}}'
                    ColorController = '{"type": "AlexaInterface","interface": "Alexa.ColorController","version": "3","properties": {"supported": [{"name": "color"}],"proactivelyReported": true,"retrievable": true}}'
                    ColorTemperatureController = '{"type": "AlexaInterface","interface": "Alexa.ColorTemperatureController","version": "3","properties": {"supported": [{"name": "colorTemperatureInKelvin"}],"proactivelyReported": true,"retrievable": true}}'
                    PercentageController = '{"type": "AlexaInterface","interface": "Alexa.PercentageController","version": "3","properties": {"supported": [{"name": "percentage"}],"proactivelyReported": true,"retrievable": true}}'
                    PowerController = '{"type": "AlexaInterface", "interface": "Alexa.PowerController","version": "3","properties": {"supported": [{"name": "powerState"}],"proactivelyReported": true,"retrievable": true}}'
                    PowerLevelController = '{"type": "AlexaInterface","interface": "Alexa.PowerLevelController","version": "3","properties": {"supported": [{"name": "powerLevel"}],"proactivelyReported": true,"retrievable": true}}'
                    #RangeController = '{"type": "AlexaInterface","interface": "Alexa.RangeController","instance": "Fan.Speed","version": "3","properties": {"supported": [{"name": "rangeValue"}],"proactivelyReported": true,"retrievable": true,"nonControllable": false},"capabilityResources": {"friendlyNames": [{"@type": "asset","value": {"assetId": "Alexa.Setting.FanSpeed"}}]},"configuration": {"supportedRange": {"minimumValue": 1,"maximumValue": 10,"precision": 1},"presets": [{"rangeValue": 10,"presetResources": {"friendlyNames": [{"@type": "asset","value": {"assetId": "Alexa.Value.Maximum"}},{"@type": "asset","value": {"assetId": "Alexa.Value.High"}},{"@type": "text","value": {"text": "highest","locale": "en-US"}}]}}]}}'
                    RangeController = '{"type": "AlexaInterface","interface": "Alexa.RangeController","version": "3","instance": "SampleManufacturer.Fan.Speed","capabilityResources": {"friendlyNames": [{"@type": "text","value": {"text": "Fan Speed","locale": "en-IN"}},{"@type": "text","value": {"text": "Air Speed","locale": "en-IN"}},{"@type": "text","value": {"text": "Speed","locale": "en-IN"}}]},"properties": {"supported": [{"name": "rangeValue"}],"proactivelyReported": true,"retrievable": true},"configuration": {"supportedRange": {"minimumValue": 1,"maximumValue": 10,"precision": 1},"presets": [{"rangeValue": 1,"presetResources": {"friendlyNames": [{"@type": "asset","value": {"assetId": "Alexa.Value.Low"}},{"@type": "asset","value": {"assetId": "Alexa.Value.Minimum"}}]}},{"rangeValue": 10,"presetResources": {"friendlyNames": [{"@type": "asset","value": {"assetId": "Alexa.Value.High"}},{"@type": "asset","value": {"assetId": "Alexa.Value.Maximum"}}]}}]}}'
                    TemperatureSensor = '{"type": "AlexaInterface","interface": "Alexa.TemperatureSensor","version": "3","properties": {"supported": [{"name": "temperature"}],"proactivelyReported": true,"retrievable": true}}' 
                    ThermostatController = '{"type": "AlexaInterface","interface": "Alexa.ThermostatController","version": "3","properties": {"supported": [{"name": "lowerSetpoint"},{"name": "upperSetpoint"},{"name": "thermostatMode"}],"proactivelyReported": true,"retrievable": true},"configuration": {"supportedModes": [ "HEAT", "COOL", "AUTO" ],"supportsScheduling": false}}'
                    AlexaInterface = '{"type": "AlexaInterface","interface": "Alexa","version": "3"}'
                    if(displayCategories == "LIGHT"):
                        x = json.loads(PowerController)
                        temp.append(x)
                        x = json.loads(BrightnessController)
                        temp.append(x)
                        x = json.loads(ColorController)
                        temp.append(x)
                        # x = json.loads(ColorTemperatureController)
                        # temp.append(x)
                        x = json.loads(AlexaInterface)
                        temp.append(x)
                        y['capabilities'] = temp
                    elif(displayCategories == "FAN"):
                        x = json.loads(PowerController)
                        temp.append(x)
                        x = json.loads(RangeController)
                        temp.append(x)
                        x = json.loads(AlexaInterface)
                        temp.append(x)
                        y['capabilities'] = temp
                    elif(displayCategories == "SWITCH"):
                        x = json.loads(PowerController)
                        temp.append(x)
                        x = json.loads(AlexaInterface)
                        temp.append(x)
                        y['capabilities'] = temp
                    elif(displayCategories == "OTHER"):
                        x = json.loads(PowerController)
                        temp.append(x)
                        x = json.loads(AlexaInterface)
                        temp.append(x)
                        y['capabilities'] = temp
                    elif(displayCategories == "MUSIC_SYSTEM"):
                        x = json.loads(PowerController)
                        temp.append(x)
                        x = json.loads(AlexaInterface)
                        temp.append(x)
                        y['capabilities'] = temp
                    elif(displayCategories == "TV"):
                        x = json.loads(PowerController)
                        temp.append(x)
                        x = json.loads(AlexaInterface)
                        temp.append(x)
                        y['capabilities'] = temp
                    elif(displayCategories == "THERMOSTAT"):
                        x = json.loads(TemperatureSensor)
                        temp.append(x)
                        x = json.loads(ThermostatController)
                        temp.append(x)
                        x = json.loads(AlexaInterface)
                        temp.append(x)
                        y['capabilities'] = temp
                    
                    xx =  '{"endpointId": "123","manufacturerName": "123","description": "123","friendlyName": "123","displayCategories": ["123"],"cookie": {},"capabilities" : ["123"]}'
                    yy = json.loads(xx)
                    yy['endpointId'] = endpointId
                    yy['manufacturerName'] = manufacturerName
                    yy['description'] = description
                    yy['friendlyName'] = friendlyName
                    yy['displayCategories'][0] = displayCategories
                    yy['capabilities'] = temp
                    #finalEndpoint = json.dumps(yy)
                    #print (finalEndpoint)
                    cap = ""
                    temp = ""
                    temp1 = ""
                    y = ""
                    #print (yy)
                    finalEndpoint = json.dumps(yy)
                    xy = json.loads(finalEndpoint)
                    temp12.append(xy)
                # print (temp12)
                d = '{"event": {"header": {"namespace": "Alexa.Discovery","name": "Discover.Response","payloadVersion": "3","messageId": "androot"},"payload": {"endpoints": ["123"]}}}'
                dd = json.loads(d)
                dd["event"]["payload"]["endpoints"] = temp12
                finalEndpoint = json.dumps(dd)
                return dd

                
            elif request["directive"]["header"]["name"] == "AcceptGrant":
                code = request["directive"]['payload']['grant']['code']
                data = {'grant_type':'authorization_code','code': code , 'client_id':'amzn1.application-oa2-client.5a03bf6fca8d467d8211b541578b8ae8','client_secret':'1c9027cd26cc3a57c527471ec1ae44391755e22fa22ecd7fdd9786e10dceb3c6'}
                r = requests.post("https://api.amazon.com/auth/o2/token",data)
                mqtt_broker_ip = "tailor.cloudmqtt.com"
                client = mqtt.Client("cloudmqtt"  + str(random.randint(1,1000)))
                client.username_pw_set("ffbqwwfa","PAC8F72zynig")
                client.on_connect = on_connect
                client.connect(mqtt_broker_ip, 13582)
                client.publish("test",str(r.text))
                print("AcceptGrant")            
                return {"event": {"header": {"messageId": "abc-123-def-456","namespace": "Alexa.Authorization","name": "AcceptGrant.Response","payloadVersion": "3"},"payload": {}}}
                
            elif request["directive"]["header"]["name"] == "ReportState":
                messageId = request["directive"]["header"]["messageId"]
                print (messageId)
                correlationToken = request["directive"]["header"]["correlationToken"]
                print (correlationToken)
                token = request["directive"]["endpoint"]["scope"]["token"]
                print (token)
                endpointId = request["directive"]["endpoint"]["endpointId"]
                print (endpointId)
                now = datetime.now()
                time = now.strftime("%Y-%m-%dT%H:%M:%S%Z")
                time = time +'Z'
                print (time)
                client = boto3.client('dynamodb')
                DB =     boto3.resource('dynamodb')
                table = DB.Table('device')
                response = table.scan(
                    FilterExpression=Key('api_key').eq(endpointId)
                )
                category = response['Items'][0]['displayCategories']
                print (category)
                
                if (category == "LIGHT"):
                    valuePower = response['Items'][0]['statusPower']
                    print (valuePower)
                    valueBright = response['Items'][0]['statusBright']
                    print (valueBright)
                    valueHue = response['Items'][0]['hue']
                    print (valueHue)
                    valueSaturation = response['Items'][0]['saturation']
                    print (valueSaturation)
                    valueBrightness = response['Items'][0]['brightness']
                    print (valueBrightness)
                    valueBrightness = response['Items'][0]['brightness']
                    print (valueBrightness)
                    return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"scope": {"type": "BearerToken","token": token},"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.PowerController","name": "powerState","value": valuePower,"timeOfSample": time,"uncertaintyInMilliseconds": 0},{"namespace": "Alexa.BrightnessController","name": "brightness","value": valueBright,"timeOfSample": time,"uncertaintyInMilliseconds": 1000},{"namespace": "Alexa.ColorController","name": "color","value": {"hue": valueHue,"saturation": valueSaturation,"brightness": valueBrightness},"timeOfSample": time,"uncertaintyInMilliseconds": 500}]}}
                                
                elif(category == "FAN"):
                    valuePower = response['Items'][0]['statusPower']
                    print (valuePower)
                    valueSpeed = response['Items'][0]['statusSpeed']
                    print (valueSpeed)
                    return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"scope": {"type": "BearerToken","token": token},"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.RangeController","instance": "Fan.Speed","name": "rangeValue","value": valueSpeed,"timeOfSample": time,"uncertaintyInMilliseconds": 500},{"namespace": "Alexa.PowerController","name": "powerState","value": valuePower,"timeOfSample": time,"uncertaintyInMilliseconds": 0}]}}
                
                elif (category == "SWITCH"):
                    valuePower = response['Items'][0]['statusPower']
                    print (valuePower)
                    return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"scope": {"type": "BearerToken","token": token},"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.PowerController","name": "powerState","value": valuePower,"timeOfSample": time,"uncertaintyInMilliseconds": 0}]}}

                elif (category == "OTHER"):
                    valuePower = response['Items'][0]['statusPower']
                    print (valuePower)
                    return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"scope": {"type": "BearerToken","token": token},"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.PowerController","name": "powerState","value": valuePower,"timeOfSample": time,"uncertaintyInMilliseconds": 0}]}}

                elif (category == "MUSIC_SYSTEM"):
                    valuePower = response['Items'][0]['statusPower']
                    print (valuePower)
                    return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"scope": {"type": "BearerToken","token": token},"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.PowerController","name": "powerState","value": valuePower,"timeOfSample": time,"uncertaintyInMilliseconds": 0}]}}

                elif (category == "TV"):
                    valuePower = response['Items'][0]['statusPower']
                    print (valuePower)
                    return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"scope": {"type": "BearerToken","token": token},"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.PowerController","name": "powerState","value": valuePower,"timeOfSample": time,"uncertaintyInMilliseconds": 0}]}}
                    
                # elif (category == "SWITCH" or category == "OTHER" or category == "MUSIC_SYSTEM" or category == "TV"):
                #     valuePower = response['Items'][0]['statusPower']
                #     print (valuePower)
                #     return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"scope": {"type": "BearerToken","token": token},"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.PowerController","name": "powerState","value": valuePower,"timeOfSample": time,"uncertaintyInMilliseconds": 0}]}}
                    
                elif(category == "THERMOSTAT"):
                    valueTemp = response['Items'][0]['statusTemp']
                    #valueTemp = float(value)
                    print (valueTemp)
                    return {"event": {"header": {"namespace": "Alexa","name": "StateReport","messageId": messageId,"correlationToken": correlationToken,"payloadVersion": "3"},"endpoint": {"endpointId": endpointId},"payload": {}},"context": {"properties": [{"namespace": "Alexa.ThermostatController","name": "targetSetpoint","value": {"value": valueTemp,"scale": "CELSIUS"},"timeOfSample": time,"uncertaintyInMilliseconds": 500}]}}
            else:
                response = handle_non_discovery_v3(request)

            
            
        else:
            logger.info("Received v2 directive!")
            print ("Please send v3 directives... This is v2, it ")

        logger.info("Response:")
        logger.info(json.dumps(response, indent=4, sort_keys=True))

        if version == "3":
            logger.info("Validate v3 response")
            validate_message(request, response)
        return response

    except ValueError as error:
        logger.error(error)
        raise


def get_uuid():
    return str(uuid.uuid4())

# v3 handlers
def get_user_info(access_token):
    #print access_token
    amazonProfileURL = 'https://api.amazon.com/user/profile?access_token='
    r = requests.get(url=amazonProfileURL+access_token)
    if r.status_code == 200:
        return r.json()
    else:
        return False

def handle_non_discovery_v3(request):
    request_namespace = request["directive"]["header"]["namespace"]
    request_name = request["directive"]["header"]["name"]
    access_token = request['directive']['endpoint']['scope']['token']
    user_details = get_user_info(access_token)
    try :
            email = user_details['email']
    except :
            email = None
    topic = ""
    msg = ""
    namespace = ""
    value = ""
    endpointid = request["directive"]["endpoint"]["endpointId"]
    print (endpointid)    
    
    if request_namespace == "Alexa.PowerController":
        namespace = "Alexa.PowerController"
        name = "powerState"   
        mqtt_broker_ip = "tailor.cloudmqtt.com"
        client = mqtt.Client("cloudmqtt"  + str(random.randint(1,1000)))
        client.username_pw_set("ffbqwwfa","PAC8F72zynig")
        client.on_connect = on_connect
        client.connect(mqtt_broker_ip, 13582)
        #client.publish("test",endpointid)
        if request_name == "TurnOn":
            value = "ON"
            client = boto3.client('dynamodb')
            DB =     boto3.resource('dynamodb')
            table = DB.Table('device')
            response = table.update_item(
                Key={
                    'api_key': endpointid
                },
                UpdateExpression="set statusPower=:p",
                ExpressionAttributeValues={
                    ':p': value
                },
                ReturnValues="UPDATED_NEW"
            )
            topic = endpointid
            msg = "TURNON"
                
        else:
            value = "OFF"
            client = boto3.client('dynamodb')
            DB =     boto3.resource('dynamodb')
            table = DB.Table('device')
            response = table.update_item(
                Key={
                    'api_key': endpointid
                },
                UpdateExpression="set statusPower=:p",
                ExpressionAttributeValues={
                    ':p': value
                },
                ReturnValues="UPDATED_NEW"
            )
            topic = endpointid
            msg = "TURNOFF"
            
    elif request_namespace == 'Alexa.RangeController':
        namespace = "Alexa.RangeController"
        name = "rangeValue"
        if request_name == 'SetRangeValue':
            now = datetime.now()
            time = now.strftime("%Y-%m-%dT%H:%M:%S%Z")
            time = time +'Z'
            print (time)
            rangeV = request['directive']['payload']['rangeValue']
            value = int(rangeV)
            client = boto3.client('dynamodb')
            DB =     boto3.resource('dynamodb')
            table = DB.Table('device')
            response = table.update_item(
                Key={
                    'api_key': endpointid
                },
                UpdateExpression="set statusSpeed=:s",
                ExpressionAttributeValues={
                    ':s': value
                },
                ReturnValues="UPDATED_NEW"
            )
            topic = endpointid
            msg = str(value)
            return {
              "event": {
                "header": {
                  "namespace": "Alexa",
                  "name": "Response",
                  "messageId": get_uuid(),
                  "correlationToken": request["directive"]["header"]["correlationToken"],
                  "payloadVersion": "3"
                },
                "endpoint": {
                  "scope": {
                    "type": "BearerToken",
                    "token": "access-token-from-Amazon"
                  },
                  "endpointId": request["directive"]["endpoint"]["endpointId"]
                },
                "payload": {}
              },
              "context": {
                "properties": [
                  {
                    "namespace": "Alexa.RangeController",
                    "instance": "Fan.Speed",
                    "name": "rangeValue",
                    "value": 7,
                    "timeOfSample": "2017-02-03T16:20:50.52Z",
                    "uncertaintyInMilliseconds": 500
                  }
                ]
              }
            }
            
    elif request_namespace == 'Alexa.BrightnessController':
        namespace = "Alexa.BrightnessController"
        name = "brightness"
        if request_name == 'SetBrightness':
            brightness = request['directive']['payload']['brightness']
            value = int(brightness)
            client = boto3.client('dynamodb')
            DB =     boto3.resource('dynamodb')
            table = DB.Table('device')
            response = table.update_item(
                Key={
                    'api_key': endpointid
                },
                UpdateExpression="set statusBright=:b",
                ExpressionAttributeValues={
                    ':b': value
                },
                ReturnValues="UPDATED_NEW"
            )
            topic = endpointid
            msg = str(value)
            value = abs(brightness)

    elif request_namespace == "Alexa.ThermostatController":
        namespace =  "Alexa.ThermostatController"
        name = "targetSetpoint"
        if request_name == "SetTargetTemperature":
            temp = request['directive']['payload']['targetSetpoint']['value']
            value = str(temp)
            client = boto3.client('dynamodb')
            DB =     boto3.resource('dynamodb')
            table = DB.Table('device')
            response = table.update_item(
                Key={
                    'api_key': endpointid
                },
                UpdateExpression="set statusTemp=:t",
                ExpressionAttributeValues={
                    ':t': value
                },
                ReturnValues="UPDATED_NEW"
            )
            topic = endpointid
            msg = str(value)
            value = {
                        "value": request['directive']['payload']['targetSetpoint']['value'] ,
                        "scale":request['directive']['payload']['targetSetpoint']['scale']
                    }

    elif request_namespace == "Alexa.ColorController":
        namespace = "Alexa.ColorController"
        name = "color"
        if request_name == "SetColor":
            hue = request['directive']['payload']['color']['hue']
            saturation = request['directive']['payload']['color']['saturation']
            brightness = request['directive']['payload']['color']['brightness']
            value = str(hue) + ', ' + str(saturation) + ', ' + str(brightness) 
            client = boto3.client('dynamodb')
            DB =     boto3.resource('dynamodb')
            table = DB.Table('device')
            response = table.update_item(
                Key={
                    'api_key': endpointid
                },
                UpdateExpression="set hue=:h,saturation=:s,brightness=:b",
                ExpressionAttributeValues={
                    ':h': str(hue),
                    ':s': str(saturation),
                    ':b': str(brightness)
                },
                ReturnValues="UPDATED_NEW"
            )
            topic = endpointid
            msg = str(value)
            value = {
                    "hue": request['directive']['payload']['color']['hue'],
                    "saturation":request['directive']['payload']['color']['saturation'],
                    "brightness": request['directive']['payload']['color']['brightness']
                    }
                    
    elif request_namespace == "Alexa.ColorTemperatureController":
        namespace = "Alexa.ColorTemperatureController"
        name = "colorTemperatureInKelvin"
        if request_name == "SetColorTemperature":
            colorTemperatureInKelvin = request['directive']['payload']['colorTemperatureInKelvin']
            value = str(colorTemperatureInKelvin)
            client = boto3.client('dynamodb')
            DB =     boto3.resource('dynamodb')
            table = DB.Table('device')
            response = table.update_item(
                Key={
                    'api_key': endpointid
                },
                UpdateExpression="set colorTemperatureInKelvin=:c",
                ExpressionAttributeValues={
                    ':c': str(colorTemperatureInKelvin)
                },
                ReturnValues="UPDATED_NEW"
            )
            topic = endpointid
            msg = str(value)
            value = abs(colorTemperatureInKelvin)
        
        
    elif request_namespace == "Alexa.ChannelController":
        namespace =  "Alexa.ChannelController"
        name = "channel"
        hub_pos = endpointid.find('-')
        hub = endpointid[0:hub_pos]
        if request_name == "ChangeChannel":
            if 'number' in request['directive']['payload']['channel'] :
                value = request['directive']['payload']['channel']['number'] 
            else :
                value = request['directive']['payload']['channelMetadata']['name']
            topic = hub + "/TV/remote"
            msg = endpointid + '-' + str(value)
        else :
            value = request['directive']['payload']['channelCount']
            topic = hub + "/TV/remote"
            if(int(value) > 0):
                msg = endpointid + '-' + 'C+'
            else :
                msg = endpointid + '-' + 'C-'
                
            value = "123"
        value = {   
                    "number": value
                }
    elif request_namespace == "Alexa.Speaker":
        namespace = "Alexa.Speaker"
        hub_pos = endpointid.find('-')
        hub = endpointid[0:hub_pos]
        if request_name == "AdjustVolume":
            name = "volume"
            value = request['directive']['payload']['volume']
            topic = hub + "/TV/remote"
            if(int(value) > 0):
                msg = endpointid + '-' + 'V+'
            else :
                msg = endpointid + '-' + 'V-'
            value = 5
        else :
            name = "muted"
            value = request['directive']['payload']['mute']
            topic = hub + "/TV/remote"
            msg =  endpointid + '-' + "MUTE"
            value = False
                
    
    
    elif request_namespace == "Alexa.Authorization":
        if request_name == "AcceptGrant":
            response = {
                "event": {
                    "header": {
                        "namespace": "Alexa.Authorization",
                        "name": "AcceptGrant.Response",
                        "payloadVersion": "3",
                        "messageId": "5f8a426e-01e4-4cc9-8b79-65f8bd0fd8a4"
                    },
                    "payload": {}
                }
            }
            return response

    # other handlers omitted in this example
    mqtt_broker_ip = "tailor.cloudmqtt.com"
    client = mqtt.Client("cloudmqtt"  + str(random.randint(1,1000)))
    client.username_pw_set("ffbqwwfa","PAC8F72zynig")
    client.on_connect = on_connect
    client.connect(mqtt_broker_ip, 13582)
    client.publish(topic,msg)
    client.loop_start()
    client.loop_stop()
    print (topic)
    print (msg)
    now = datetime.now()
    time = now.strftime("%Y-%m-%dT%H:%M:%S%Z")
    time = time +'Z'
    print (time)
    
    response = {
            "context": {
                "properties": [
                    {
                        "namespace": namespace ,
                        "name": name,
                        "value": value,
                        "timeOfSample": time,
                        "uncertaintyInMilliseconds": 500
                    }
                ]
            },
            "event": {
                "header": {
                    "namespace": "Alexa",
                    "name": "Response",
                    "payloadVersion": "3",
                    "messageId": get_uuid(),
                    "correlationToken": request["directive"]["header"]["correlationToken"]
                },
                "endpoint": {
                    "scope": {
                        "type": "BearerToken",
                        "token": "access-token-from-Amazon"
                    },
                    "endpointId": request["directive"]["endpoint"]["endpointId"]
                },
                "payload": {}
            }
        }
        
    return response

def get_directive_version(request):
    try:
        return request["directive"]["header"]["payloadVersion"]
    except:
        try:
            return request["header"]["payloadVersion"]
        except:
            return "-1"