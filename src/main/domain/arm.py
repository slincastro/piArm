class Arm:
    def __init__(self, waist, shoulder):
        self._vertical_joints = shoulder
        self._waist = waist

    @property
    def waist(self):
        return self._waist

    @property
    def shoulder(self):
        return self._vertical_joints

    def get_vertical_joint(self, joint_id):
        return self.filter_by_value(self._vertical_joints, joint_id)

    def filter_by_value(self, seq, value):
        for el in seq:
            if el.id == value: return el
