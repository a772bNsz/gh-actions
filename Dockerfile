FROM mottosso/maya:2018

WORKDIR /root/workdir

COPY ./ /root/workdir

ENTRYPOINT ["./entrypoint.sh"]
