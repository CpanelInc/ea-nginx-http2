# NGINX http2 support

## Target Audiences

1. Maintenance and security teams
2. Training and technical support
3. Managers and other internal key stakeholders
4. Future project/feature owners/maintainers

## Detailed Summary

Have is install and own `/etc/nginx/conf.d/http2.conf`.

It servers two purposes:

1. It tells the config gen in `ea-nginx` that we want http2 configured.
   * like an ea-nginx-standalone esque `/etc/nginx/ea-nginx/enable.http2` could do.
2. It can contain our defaults/user’s http2 configuration.
   * **unlike** like an ea-nginx-standalone esque `/etc/nginx/ea-nginx/enable.http2`

## Overall Intent

Add/Remove http2 support to NGINX easily and consistently

## Maintainability

Estimate:

1. how much time and resources will be needed to maintain the feature in the future
2. how frequently maintenance will need to happen

Answer to both: very little. only when we want to change our default http2 config options.

## Options/Decisions

1. Option 1: flag file. Con: no config
2. Option 2: conf file. Pro: can serve as flag file and contain additonal config. same amount of effort

## Child Documents

None.
