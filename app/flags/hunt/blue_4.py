from plugins.training.app.base_flag import BaseFlag


name = 'Hunt Flag 4'
challenge = 'Look to Hunt Flag 1 for instructions.\n' \
            'Ensure you enter a PId.\n\n' \
            'Tactic: Exfiltration'
extra_info = """Technique: Exfiltration Over C2 Channel"""


operation_name = 'training_hunt_4'
adversary_id = '9f0691a7-a11e-4921-9465-278d6953b316'
agent_group = 'cert-win'
verify_type = 'pid'


async def verify(services):
    return await BaseFlag.standard_hunt_flag(services, operation_name, adversary_id, agent_group, verify_type)