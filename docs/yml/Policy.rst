Policy.yml
----------

FortiOS v6.4

.. code:: yaml

    action: accept
    anti-replay: enable
    application-list: ''
    auth-cert: ''
    auth-path: disable
    auth-redirect-addr: ''
    auto-asic-offload: enable
    av-profile: ''
    block-notification: disable
    captive-portal-exempt: disable
    capture-packet: disable
    cifs-profile: ''
    comments: ''
    custom-log-fields: []
    decrypted-traffic-mirror: ''
    delay-tcp-npu-session: disable
    diffserv-forward: disable
    diffserv-reverse: disable
    diffservcode-forward: '000000'
    diffservcode-rev: '000000'
    disclaimer: disable
    dlp-sensor: ''
    dnsfilter-profile: ''
    dsri: disable
    dstaddr:
    - name: all
      q_origin_key: all
    dstaddr-negate: disable
    dstaddr6: []
    dstintf:
    - name: any
      q_origin_key: any
    email-collect: disable
    emailfilter-profile: ''
    file-filter-profile: ''
    firewall-session-dirty: check-all
    fixedport: disable
    fsso-agent-for-ntlm: ''
    fsso-groups: []
    geoip-anycast: disable
    geoip-match: physical-location
    global-label: ''
    groups: []
    http-policy-redirect: disable
    icap-profile: ''
    identity-based-route: ''
    inbound: disable
    inspection-mode: flow
    internet-service: disable
    internet-service-custom: []
    internet-service-custom-group: []
    internet-service-group: []
    internet-service-name: []
    internet-service-negate: disable
    internet-service-src: disable
    internet-service-src-custom: []
    internet-service-src-custom-group: []
    internet-service-src-group: []
    internet-service-src-name: []
    internet-service-src-negate: disable
    ippool: disable
    ips-sensor: ''
    label: ''
    logtraffic: utm
    logtraffic-start: disable
    match-vip: disable
    match-vip-only: disable
    name: POLICY_NAME
    nat: disable
    natinbound: disable
    natip: 0.0.0.0 0.0.0.0
    natoutbound: disable
    np-acceleration: enable
    ntlm: disable
    ntlm-enabled-browsers: []
    ntlm-guest: disable
    outbound: enable
    per-ip-shaper: ''
    permit-any-host: disable
    permit-stun-host: disable
    policyid: 23
    poolname: []
    poolname6: []
    profile-group: ''
    profile-protocol-options: default
    profile-type: single
    q_origin_key: 23
    radius-mac-auth-bypass: disable
    redirect-url: ''
    replacemsg-override-group: ''
    reputation-direction: destination
    reputation-minimum: 0
    rtp-addr: []
    rtp-nat: disable
    schedule: always
    schedule-timeout: disable
    send-deny-packet: disable
    service:
    - name: ALL
      q_origin_key: ALL
    service-negate: disable
    session-ttl: '0'
    src-vendor-mac: []
    srcaddr:
    - name: all
      q_origin_key: all
    srcaddr-negate: disable
    srcaddr6: []
    srcintf:
    - name: any
      q_origin_key: any
    ssh-filter-profile: ''
    ssh-policy-redirect: disable
    ssl-ssh-profile: no-inspection
    status: disable
    tcp-mss-receiver: 0
    tcp-mss-sender: 0
    tcp-session-without-syn: disable
    timeout-send-rst: disable
    tos: '0x00'
    tos-mask: '0x00'
    tos-negate: disable
    traffic-shaper: ''
    traffic-shaper-reverse: ''
    users: []
    utm-status: disable
    uuid: 1d34d556-51cf-51ec-0a55-8f9fb4bee764
    vlan-cos-fwd: 255
    vlan-cos-rev: 255
    vlan-filter: ''
    voip-profile: ''
    vpntunnel: ''
    waf-profile: ''
    wccp: disable
    webfilter-profile: ''
    webproxy-forward-server: ''
    webproxy-profile: ''
