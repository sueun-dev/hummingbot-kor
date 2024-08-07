import argparse  # argparse 모듈을 임포트하여 커맨드 라인 파싱 기능을 사용할 수 있습니다.

import path_util  # noqa: F401

from hummingbot.client.config.conf_migration import migrate_configs
from hummingbot.client.config.config_crypt import ETHKeyFileSecretManger

# path_util 모듈을 임포트합니다. 이 모듈은 사용되지 않지만, 경로 관련 유틸리티를 제공할 수 있습니다.
# 'noqa: F401' 주석은 이 라인의 코드가 린트 검사에서 무시되도록 합니다.

# migrate_configs 함수를 임포트합니다. 이 함수는 설정 파일의 마이그레이션을 처리합니다.

# ETHKeyFileSecretManger 클래스를 임포트합니다. 이 클래스는 암호화된 설정을 관리합니다.

# 스크립트가 메인 프로그램으로 실행될 때만 아래 코드를 실행합니다.
if __name__ == "__main__":
    # argparse.ArgumentParser 인스턴스를 생성하여 프로그램 설명을 추가합니다.
    parser = argparse.ArgumentParser(description="Migrate the HummingBot confs")
    # 'password' 인자를 추가합니다. 이는 마이그레이션할 암호화된 설정 파일에 필요한 비밀번호입니다.
    parser.add_argument("password", type=str, help="Required to migrate all encrypted configs.")
    # 입력받은 인자를 파싱합니다.
    args = parser.parse_args()
    # ETHKeyFileSecretManger 클래스의 인스턴스를 생성하고, 사용자로부터 입력받은 비밀번호를 전달합니다.
    secrets_manager_ = ETHKeyFileSecretManger(args.password)
    # 마이그레이션 함수를 호출하고, 생성된 비밀 관리자 인스턴스를 인자로 제공합니다.
    migrate_configs(secrets_manager_)
