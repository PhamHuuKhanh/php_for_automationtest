import yaml

with open('/config/data_config.yaml') as stream:
   data = yaml.safe_load(stream)

test = data['infomation']
test.update(dict(env="dev", platform="iOS"))

with open('/config/data_config.yaml', 'wb') as stream:
   yaml.safe_dump(data, stream, default_flow_style=False,
                  explicit_start=True, allow_unicode=True, encoding='utf-8')