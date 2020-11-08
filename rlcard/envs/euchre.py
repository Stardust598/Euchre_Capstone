from rlcard.envs import Env
from rlcard.games.euchre import Game
from rlcard.utils.euchre_utils import ACTION_SPACE, ACTION_LIST

class EuchreEnv(Env):

    def __init__(self, config):
        self.game = Game()
        self.name = "euchre"

        self.actions = ACTION_LIST
        self.state_shape = [len(self.actions)]
        super().__init__(config)

    def _extract_state(self, state):
        state['legal_actions'] = self._get_legal_actions()
        state['raw_legal_actions'] = self.game.get_legal_actions()
        state['obs'] = state
        return state

    def _decode_action(self, action_id):
        return ACTION_LIST[action_id]

    def _get_legal_actions(self):
        legal_actions = self.game.get_legal_actions()
        legal_ids = [ACTION_SPACE[action] for action in legal_actions]
        return legal_ids

    def get_payoffs(self):
        return self.game.get_payoffs()