#import configparser

#config = configparser.ConfigParser()
#config.read("testfm.properties")

from dynaconf import LazySettings
settings = LazySettings(
    envvar_prefix='TesTFM',
    core_loaders=['YAML'],
    settings_file=['settings.yaml'],
    preload=['*.yaml'],
    includes=['settings.local.yaml', '.secrets.yaml', '.secrets_*.yaml'],
    envless_mode=True,
    lowercase_read=True,
)

RHN_USERNAME = settings.subscription.RHN_USERNAME
RHN_PASSWORD = settings.subscription.RHN_PASSWORD
FM_RHN_POOLID = settings.subscription.FM_RHN_POOLID
DOGFOOD_ORG = settings.subscription.DOGFOOD_ORG
DOGFOOD_ACTIVATIONKEY = settings.subscription.DOGFOOD_ACTIVATIONKEY
CAPSULE_DOGFOOD_ACTIVATIONKEY = settings.subscription.CAPSULE_DOGFOOD_ACTIVATIONKEY
DOGFOOD_URL = settings.subscription.DOGFOOD_URL
HOTFIX_URL = settings.URLS.HOTFIX_URL
SERVER_HOSTNAME = settings.SERVER.SERVER_HOSTNAME

katello_ca_consumer = DOGFOOD_URL + "/pub/katello-ca-consumer-latest.noarch.rpm"
upstream_url = {
    "candlepin_repo": (
        "https://fedorapeople.org/groups/katello/releases/yum/3.8/candlepin/el7/x86_64/"
    ),
    "client_repo": "https://fedorapeople.org/groups/katello/releases/yum/3.8/client/el7/x86_64/",
    "katello_repo": (
        "https://fedorapeople.org/groups/katello/releases/yum/latest/katello/el7/x86_64/"
    ),
    "plugins_repo": "https://yum.theforeman.org/plugins/latest/el7/x86_64/",
    "pulp_repo": "https://fedorapeople.org/groups/katello/releases/yum/3.5/pulp/el7/x86_64/",
    "puppet_repo": "http://yum.puppetlabs.com/el/6.4/x86_64/",
    "releases_repo": "https://yum.theforeman.org/releases/latest/el7/x86_64/",
}
common_repos = [
    "rhel-7-server-rpms",
    "rhel-server-rhscl-7-rpms",
    "rhel-7-server-satellite-maintenance-6-rpms",
]
sat_64_repos = [
    "rhel-7-server-ansible-2.6-rpms",
    "rhel-7-server-satellite-6.4-rpms",
] + common_repos
sat_65_repos = [
    "rhel-7-server-ansible-2.6-rpms",
    "rhel-7-server-satellite-6.5-rpms",
] + common_repos
sat_66_repos = [
    "rhel-7-server-ansible-2.8-rpms",
    "rhel-7-server-satellite-6.6-rpms",
] + common_repos
sat_67_repos = [
    "rhel-7-server-ansible-2.8-rpms",
    "rhel-7-server-satellite-6.7-rpms",
] + common_repos
sat_68_repos = [
    "rhel-7-server-ansible-2.9-rpms",
    "rhel-7-server-satellite-6.8-rpms",
] + common_repos
sat_beta_repo = [
    "rhel-server-7-satellite-6-beta-rpms",
    "rhel-7-server-ansible-2.9-rpms",
    "rhel-7-server-satellite-maintenance-6-beta-rpms",
    "rhel-server-rhscl-7-rpms",
    "rhel-7-server-rpms",
]
cap_68_repos = [
    "rhel-7-server-ansible-2.9-rpms",
    "rhel-7-server-satellite-tools-6.8-rpms",
    "rhel-7-server-satellite-capsule-6.8-rpms",
] + common_repos
cap_beta_repo = [
    "rhel-server-7-satellite-capsule-6-beta-rpms",
    "rhel-7-server-ansible-2.9-rpms",
    "rhel-7-server-satellite-maintenance-6-beta-rpms",
    "rhel-server-rhscl-7-rpms",
    "rhel-7-server-rpms",
    "rhel-7-server-satellite-tools-6-beta-rpms",
]
sat_repos = {
    "6.4": sat_64_repos,
    "6.5": sat_65_repos,
    "6.6": sat_66_repos,
    "6.7": sat_67_repos,
    "6.8": sat_68_repos,
}
cap_repos = {
    "6.8": cap_68_repos,
}
foreman_maintain_yml = "/etc/foreman-maintain/foreman_maintain.yml"
epel_repo = "https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm"
satellite_answer_file = "/etc/foreman-installer/scenarios.d/satellite-answers.yaml"
fm_hammer_yml = "/etc/foreman-maintain/foreman-maintain-hammer.yml"
