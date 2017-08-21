class Arm:
    def __init__(self, waist, shoulder, gripper):
        self._vertical_joints = shoulder
        self._waist = waist
        self._gripper = gripper

    @property
    def waist(self):
        return self._waist

    @property
    def shoulder(self):
        return self._vertical_joints

    @property
    def gripper(self):
        return self._gripper

    def get_vertical_joint(self, joint_id):
        return self.filter_by_value(self._vertical_joints, joint_id)

    def filter_by_value(self, seq, value):
        for el in seq:
            if el.id == value: return el
