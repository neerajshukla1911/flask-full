import logging
from flask import jsonify
from app.tasks import task_1


logger = logging.getLogger(__name__)


def demo_api():
    """
    Skill
    ---
    parameters:
     - name: data
       in: body
       required: true
       type: json
    """
    logger.debug("in demo api")
    task_1.delay()
    return jsonify({'message': "demo get api"}), 200
